/*
 * /usr/local/cuda-8.0/bin/nvcc -Xcompiler -Wall -O3 -arch sm_61 -std=c++11 -o use_shared use_shared.cu
 *
 * We have N (in the order of 30_000) real numbers and M entities (in the order
 * of 2_000_000). We have associations between entities and numbers (that is,
 * an entity is associated with some of the N numbers).  The average number of
 * associations for an entity is in the order of 10, with an upper bound equal
 * to MAX_M2N, around 100).  The N numbers in are in the array 'numbers' and
 * the associations are in the array 'map'. 'map' is an array of M lists, the
 * lists are stored in fixed-size arrays and contain indices to the array
 * 'numbers' (-1 is used for sentinel values trailing in the arrays).
 *
 * We want to build an array of M real numbers where each element indexed by m
 * is obtained by the product of the elements in 'numbers' in the list map[m].
 * A picture is worth a thousand words:
 *
 * Suppose the array of size N is in general numbers[0] numbers[1] ... numbers[N-1]
 *
 * and an example of the map is
 *
 * m=0   10 67 13 -1 -1 -1 ...
 * m=1   0 -1 -1 -1 -1 -1 ....
 * m=2   1 5 10 23 ....
 * ...   ......
 *
 * then the three first elements of the desired array are given by
 *
 *    result[0] = numbers[10] * numbers[67] * numbers[13]
 *    result[1] = numbers[0]
 *    result[2] = numbers[1] * numbers[5] * numbers[10] * numbers[23] * ...
 *
 * This program implements this algorithm in the gpu with cuda. Two kernels are
 * provided: one of them leverages shared memory to cache the map while the
 * other reads it directly from global memory when making the computations.
 *
 * Very interestingly, we note that the performance gap between the kernels w/
 * and w/o shared memory depends on the variance of the distribution of the
 * number of associations (see num_associations_dis). When the number of
 * associations is constant (drawn from a uniform [MAX_M2N, MAX_M2N]), the
 * kernel w/ shared memory is best. On the other hand, when a uniform [0,
 * MAX_M2N] is used, the kernel w/o shared memory performs better.
 *
 */

#include <algorithm>
#include <array>
#include <chrono>
#include <cmath>
#include <cstring>
#include <iostream>
#include <random>

#define CUDA_CALL(F) if ((F) != cudaSuccess) { printf("Cuda call error %s at %s:%d\n", cudaGetErrorString(cudaGetLastError()), __FILE__, __LINE__); abort(); }
#define CUDA_CHECK_CALL() { auto err = cudaGetLastError(); if (err != cudaSuccess) { printf("Cuda check call error %s at %s:%d\n", cudaGetErrorString(err), __FILE__, __LINE__-1); abort(); } }

using real = float;

const short N = 32768 - 1;
const size_t M = 1024 * 2048;
const unsigned char MAX_M2N = 80;
const size_t BLOCK_DIM = 256;

std::default_random_engine gen;

std::array<real, N> numbers;
real* dev_numbers;

std::array<short, M * MAX_M2N> map;
short* dev_map;

real* dev_result;
real* dev_result_with_shared;

std::array<real, M> result;
std::array<real, M> result_with_shared;

void FillNumbers()
{
  std::uniform_real_distribution<real> dis{0, 1};
  std::for_each(numbers.begin(), numbers.end(), [&dis](real& number) { number = dis(gen); });
}

void FillMap()
{
  std::memset(map.data(), -1, map.size() * sizeof(short));

  std::uniform_int_distribution<int> num_associations_dis{0, MAX_M2N};
  std::uniform_int_distribution<short> associations_dis{0, N-1};

  for (size_t i = 0; i < M; i++) {
    unsigned char num_associations = num_associations_dis(gen);
    std::for_each(map.begin() + i * MAX_M2N, map.begin() + i * MAX_M2N + num_associations,
                  [&associations_dis](short& item) { item = associations_dis(gen); });
  }
}

__global__ void kernel(real* dev_result, const real* dev_numbers, const short* dev_map)
{
  const int idx = blockIdx.x * blockDim.x + threadIdx.x;
  if (idx < M) {
    real val = 1.0;
    const short* map = dev_map + idx * MAX_M2N;
    for (unsigned char i = 0; i < MAX_M2N; i++) {
      short item = *map++;
      if (item == -1) break;
      val *= dev_numbers[item];
    }

    dev_result[idx] = val;
  }
}

__global__ void kernel_with_shared(real* dev_result_with_shared, const real* dev_numbers, const short* dev_map)
{
  const int idx = blockIdx.x * blockDim.x + threadIdx.x;
  if (idx < M) {
    __shared__ short map_cache[BLOCK_DIM * MAX_M2N];
    const short* map = dev_map + idx * MAX_M2N;
    for (unsigned char i = 0; i < MAX_M2N; i++) {
      short item = *map++;
      map_cache[threadIdx.x * MAX_M2N + i] = item;
      if (item == -1) break;
    }

    __syncthreads();

    real val = 1.0;
    for (unsigned char i = 0; i < MAX_M2N; i++) {
      short item = map_cache[threadIdx.x * MAX_M2N + i];
      if (item == -1) break;
      val *= dev_numbers[item];
    }

    dev_result_with_shared[idx] = val;
  }
}

int main()
{
  {
    std::random_device r;
    gen = std::default_random_engine(r());
  }

  FillNumbers();
  FillMap();

  CUDA_CALL(cudaMalloc(&dev_numbers, N * sizeof(real)));
  CUDA_CALL(cudaMalloc(&dev_map, M * MAX_M2N * sizeof(short)));
  CUDA_CALL(cudaMalloc(&dev_result, M * sizeof(real)));
  CUDA_CALL(cudaMalloc(&dev_result_with_shared, M * sizeof(real)));

  CUDA_CALL(cudaMemcpy(dev_numbers, numbers.data(), N * sizeof(real), cudaMemcpyHostToDevice));
  CUDA_CALL(cudaMemcpy(dev_map, map.data(), M * MAX_M2N * sizeof(short), cudaMemcpyHostToDevice));

  const int num_threads = BLOCK_DIM;
  const int num_blocks = M / num_threads;

  auto kernel_start = std::chrono::high_resolution_clock::now();
  for (int i = 0; i < 100; i++) {
    kernel<<<num_blocks, num_threads>>>(dev_result, dev_numbers, dev_map);
    CUDA_CHECK_CALL();
    CUDA_CALL(cudaDeviceSynchronize());
  }
  auto kernel_finish = std::chrono::high_resolution_clock::now();

  for (int i = 0; i < 100; i++) {
    kernel_with_shared<<<num_blocks, num_threads>>>(dev_result_with_shared, dev_numbers, dev_map);
    CUDA_CHECK_CALL();
    CUDA_CALL(cudaDeviceSynchronize());
  }
  auto kernel_with_shared_finish = std::chrono::high_resolution_clock::now();

  CUDA_CALL(cudaMemcpy(result.data(), dev_result, M * sizeof(real), cudaMemcpyDeviceToHost));
  CUDA_CALL(cudaMemcpy(result_with_shared.data(), dev_result_with_shared, M * sizeof(real), cudaMemcpyDeviceToHost));

  double diff = 0;
  for (size_t i = 0; i < result.size(); i++) diff += std::abs(result[i] - result_with_shared[i]);
  std::cout << "Result difference: " << diff << '.' << std::endl;

  std::cout << std::chrono::duration_cast<std::chrono::milliseconds>(kernel_finish - kernel_start).count() << ' '
            << std::chrono::duration_cast<std::chrono::milliseconds>(kernel_with_shared_finish - kernel_finish).count() << '\n';

  CUDA_CALL(cudaFree(dev_numbers));
  CUDA_CALL(cudaFree(dev_map));
  CUDA_CALL(cudaFree(dev_result));
  CUDA_CALL(cudaFree(dev_result_with_shared));
}
