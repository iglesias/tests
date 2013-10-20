#include <iostream>
#include <set>

int main()
{
  std::set<int> s;
  for (int i = 0; i < 5; i++) s.insert(i);
  std::set<int>::iterator it = s.begin();
  std::cout << *it << std::endl;
  std::set<int>::iterator jt = ++it;
  jt++;
  std::cout << *it << std::endl;
  std::cout << *jt << std::endl;
}
