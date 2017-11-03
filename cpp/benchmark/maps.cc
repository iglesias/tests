// Dependent on http://github.com/google/benchmark
// g++ -Ofast -std=c++11 maps.cc -lbenchmark -pthread

#include <cstdlib>
#include <map>
#include <unordered_map>

#include "benchmark/benchmark.h"

const int WIDTH = 2332;
const int HEIGHT = 1752;

using Key = std::pair<int, int>;

template <class Container>
void Fill(Container* container) {
  for (int i = 0; i < WIDTH; i++)
    for (int j = 0; j < HEIGHT; j++)
      container->insert({{i, j}, i * HEIGHT + j});
}

struct KeyCmp {
  bool operator()(const Key& lhs, const Key& rhs) const {
    if (lhs.first == rhs.first)
      return lhs.second < rhs.second;
    else
      return lhs.first < rhs.first;
  }
};

struct KeyHash {
  std::size_t operator()(const Key& k) const {
    return k.first * HEIGHT + k.second;
  }
};

struct KeyEqual {
  bool operator()(const Key& lhs, const Key& rhs) const {
    return lhs.first == rhs.first && lhs.second == rhs.second;
  }
};

void UseMap(benchmark::State& state) {
  std::map<Key, int, KeyCmp> container;
  Fill(&container);

  while (state.KeepRunning())
    container.find({std::rand() % WIDTH, std::rand() % HEIGHT});
}
BENCHMARK(UseMap);

void UseUnorderedMap(benchmark::State& state) {
  std::unordered_map<Key, int, KeyHash, KeyEqual> container;
  Fill(&container);

  while (state.KeepRunning())
    container.find({std::rand() % WIDTH, std::rand() % HEIGHT});
}
BENCHMARK(UseUnorderedMap);

BENCHMARK_MAIN();
