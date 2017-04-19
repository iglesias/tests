/*
 * cuda_innvalid_symbol_error.cu
 *
 * Compilation triggering runtime error:
 *  nvcc -gencode arch=compute_52,code=sm_52 -std=c++11 cuda_invalid_symbol_error.cu -o cuda_invalid_symbol_error
 *
 * Error-free compilation:
 *  nvcc -arch=sm_52 -std=c++11 cuda_invalid_symbol_error.cu -o cuda_invalid_symbol_error
 *
 * http://stackoverflow.com/questions/42813955/invalid-device-symbol-error-depending-on-nvcc-flags
 */

#include <iostream>
#include <vector>

// Matrix side size (they are square).
const int N = 3;
const int num_mats = 14;

// Rotation matrices.
__constant__ float rot_mats_device[num_mats * N * N];

int main() {
  auto errSetDevice = cudaSetDevice(0);
  if (errSetDevice != cudaSuccess) {
    std::cout << "SetDevice error: " << cudaGetErrorString(errSetDevice)
              << std::endl;
  }

  std::vector<float> rot_mats_host(num_mats * N * N);
  for (int i = 0; i < rot_mats_host.size(); i++) rot_mats_host[i] = i;

  auto errMemcpyToSymbol = cudaMemcpyToSymbol(
      rot_mats_device, rot_mats_host.data(), sizeof(rot_mats_device));

  if (errMemcpyToSymbol != cudaSuccess) {
    std::cout << "MemcpyToSymbol error: "
              << cudaGetErrorString(errMemcpyToSymbol) << std::endl;
  }
}
