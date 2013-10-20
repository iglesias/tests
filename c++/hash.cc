#include <functional>
#include <iostream>
#include <string>

int main()
{
  std::hash<std::string> hash_fn;
  std::cout << hash_fn(std::to_string((double) 1.0)) << std::endl;
  std::cout << hash_fn(std::to_string((float) 1.0)) << std::endl;
  std::cout << hash_fn(std::to_string((int) 1)) << std::endl;
}
