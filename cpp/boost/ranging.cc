// g++ -std=c++14 -Wall -o ranging ranging.cc
// tested with boost 1.68.0 and g++ 4.9.3
// c++14 is used for the generic lambda

#include <iostream>
#include <vector>

#include "boost/range/adaptors.hpp"

int main()
{
  std::vector<int> v{1, 2, 3, 4, 5};
  for (auto&& item : v | boost::adaptors::indexed())
    std::cout << item.index() << ' ' << item.value() << '\n';

  auto range_with_preceded = v | boost::adaptors::indexed() | boost::adaptors::filtered([](auto&& item) { return item.index() > 0; });
  for (auto&& item : range_with_preceded)
    std::cout << item.index() << ' ' << item.value() << '\n';
}
