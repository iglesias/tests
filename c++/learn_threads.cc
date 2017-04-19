#include <chrono>
#include <iostream>
#include <thread>

void foo() {
  // simulate expensive operation
  std::this_thread::sleep_for(std::chrono::seconds(5));
}

void bar() {
  // simulate expensive operation
  std::this_thread::sleep_for(std::chrono::seconds(10));
}

int main() {
  std::cout << "starting first helper...\n";
  std::thread helper1(foo);

  std::cout << "starting second helper...\n";
  std::thread helper2(bar);

  std::cout << "waiting for helpers to finish..." << std::endl;
  helper1.join();
  helper2.join();

  std::cout << "the helpers have finished! We wait a bit more" << std::endl;
  std::this_thread::sleep_for(std::chrono::seconds(10));

  std::cout << "done!\n";
}
