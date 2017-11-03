/*
 * learn_decltype.cc
 * g++ -std=c++14 -Wall learn_decltype.cc -o learn_decltype
 * ./learn_decltype | c++filt -t
 */

#include <iostream>
#include <typeinfo>

template<typename T, typename U>
auto add(T t, U u) -> decltype(t + u);

int main()
{
  std::cout << typeid(add(5,3)).name() << std::endl;
  std::cout << typeid(add(float(5), 3)).name() << std::endl;
}

template<typename T, typename U>
auto add(T t, U u) // c++11 needs trailing return type also here.
{
  return t+u;
}
