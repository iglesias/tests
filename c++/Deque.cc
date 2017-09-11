#include <cstdio>
#include <deque>
#include <typeinfo>

int main() {
  std::deque<int> int_deque;
  printf("%s %s\n", typeid(int_deque).name(), typeid(std::deque<int>).name());
  for (int i = 0; i < 10; ++i) {
    if (i % 2 == 0)
      int_deque.push_front(i);
    else
      int_deque.push_back(i);
  }

  while (!int_deque.empty()) {
    printf("%d%c", int_deque.front(), int_deque.size() == 1 ? '\0' : ' ');
    int_deque.pop_front();
  }
  printf("\n");

  for (int i = 0; i < 10; ++i) int_deque.push_back(i);

  for (auto it = int_deque.begin(); it != int_deque.end(); ++it)
    printf("%d ", *it);
  printf("\n");
}
