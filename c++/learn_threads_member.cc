// g++ -std=c++11 -Wall -o learn_threads_member learn_threads_member.cc -pthread

#include <chrono>
#include <iostream>
#include <thread>

const int NUM_WORKERS = 5;

class A {
 public:
  void LaunchThreads();
  void DoWork();

 private:
  std::thread threads_[NUM_WORKERS];
};

static void DoWork(A* a) { a->DoWork(); }

void A::LaunchThreads() {
  for (int i = 0; i < NUM_WORKERS; i++) {
    threads_[i] = std::thread(::DoWork, this);
  }

  for (int i = 0; i < NUM_WORKERS; i++) {
    threads_[i].join();
  }
}

void A::DoWork() {
  std::cout << "Starting DoWork\n";
  std::this_thread::sleep_for(std::chrono::seconds(10));
  std::cout << "Finishing DoWork\n";
}

int main() {
  A a;
  a.LaunchThreads();
  a.LaunchThreads();
}
