#include <algorithm>
#include <cassert>
#include <cstdio>
#include <functional>
#include <iostream>
#include <random>
#include <utility>
#include <vector>

#define PRINT_VECTOR(v) \
  for (std::size_t i = 0; i < v.size(); i++) \
    std::cout << v[i] << (i == v.size()-1 ? '\n' : ' ');

std::default_random_engine gen((std::random_device())());

template<typename T>
T find_kth_largest(std::vector<T>* input, const std::size_t k, const int l, const int r)
{
//  printf("l=%d r=%d\n", l, r);
  if (l == r) return input->at(l);

  assert(l < r);
  const int p = std::uniform_int_distribution<>{l, r}(gen);
  const T pivot = input->at(p);
//  printf("p=%d\n", p);
  int i = l;
  std::swap(input->at(p), input->at(r));
  for (int j = l; j < r; j++) {
    if (input->at(j) > pivot) std::swap(input->at(j), input->at(i++));
  }

  std::swap(input->at(i), input->at(r));
//  printf("i=%d k=%lu\n", i, k);

  if (i == k-1)   return input->at(i);
  else if (i >= k) return find_kth_largest(input, k, l, i-1);
  else            return find_kth_largest(input, k, i+1, r);
}

//FIXME template comparison function.
template<typename T>
T find_kth_largest(std::vector<T>* input, const std::size_t k)
{
  return find_kth_largest(input, k, 0, input->size()-1);
}

int main(int argc, char** argv)
{
  std::size_t size = std::uniform_int_distribution<>{1, 50}(gen);
  if (argc > 1) size = atoi(argv[1]);
  assert(size > 0);

  std::vector<unsigned int> input(size);
  for (auto& item : input) item = std::uniform_int_distribution<>{0, 1000}(gen);

  std::size_t k = std::uniform_int_distribution<>{1, static_cast<int>(input.size())}(gen);
  if (argc > 2) k = atoi(argv[2]);
  assert(k > 0);
//  printf("k=%lu\n", k);

  using input_type = decltype (input)::value_type;
  const input_type& kth_largest = find_kth_largest(&input, k);

  // Testing the solution found.
  std::sort(input.begin(), input.end(), std::greater<input_type>());
  std::cout << "Solutions " << (kth_largest == input[k-1] ? "do" : "do not") << " match!\n";
}
