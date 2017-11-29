#include <iostream>
#include <thread>
#include <vector>

template <typename Function>
void parallel_f(int num_iters, int max_threads, Function f)
{
  std::vector<std::thread> threads(max_threads);

  int iter = 0;
  while (iter < num_iters) {
    for (size_t i = 0; i < threads.size(); i++) {
      threads[i] = std::thread(f, iter++);
      if (iter >= num_iters) break;
    }

    for (size_t i = 0; i < threads.size(); i++) {
      if (threads[i].joinable()) threads[i].join();
    }
  }
}

class A {
 public:
  A()
  {
    std::cout << "Building\n";
    count = new int;
    *count = 0;
  }

  A(const A& other) {
    std::cout << "Copying\n";
    count = new int;
    *count = *(other.count);
  }

  A(A&& other) {
    std::cout << "Moving\n";
    count = other.count;
    other.count = nullptr;
  }

  A& operator=(const A& other)
  {
    std::cout << "Copy-assigning\n";
    count = other.count;
    return *this;
  }

  A& operator=(A&& other)
  {
    std::cout << "Move-assigning\n";
    count = other.count;
    other.count = nullptr;
    return *this;
  }

  ~A() {
    std::cout << "Destroying\n";
    delete count;
  }

  void increment() { (*count)++; }

  int get() const
  {
    return *count;
  }
 
 private:
  int* count;
};

int main()
{
  int num_iters = 14;
  int max_threads = 6;

  std::vector<A> as(num_iters);

  parallel_f(num_iters, max_threads, [&](int i){
      as[i].increment();
  });

  for (const auto& a : as) std::cout << a.get() << std::endl;
}
