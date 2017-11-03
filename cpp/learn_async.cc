#include <chrono>
#include <cstdlib>
#include <future>
#include <iostream>

int f() {
  // simulate expensive operation
  std::this_thread::sleep_for(std::chrono::seconds(3));
  std::srand(std::time(0));
  return std::rand() % 10;
}

int main() {
  // executes f in a new thread
  auto handle = std::async(std::launch::async, f);

  // executes f in this thread
  // auto handle = std::async(std::launch::deferred, f);

  // handle = std::async(f);
  // equivalent to
  // std::async(std::launch::async | std::launch::deferred, f);
  // implementation dependent (takeaway, better ignore and use one
  // of the previous forms).

  std::cout << handle.get() << std::endl;
}
