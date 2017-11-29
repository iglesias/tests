#include <cassert>
#include <cstddef>
#include <iostream>

template<typename T>
class list {
 public:
  list() : m_front(nullptr), m_back(nullptr), m_size(0) { }

  ~list() {
    node* cur_node = m_front;
    while (cur_node) {
      node* aux = cur_node;
      cur_node = cur_node->next;
      delete aux;
    }
  }

  void push_back(const T& new_item) {
    node* new_node = new node(nullptr, m_back, new_item);
    if (m_size == 0) m_front = new_node;
    if (m_size == 1) m_front->next = new_node;
    if (m_size > 0) m_back->next = new_node;
    m_back = new_node;
    m_size++;
  }

  size_t size() const { return m_size; }

  T get_item_from_the_end(size_t M) {
    assert(M > 0 && M <= m_size);
    const node* cur_node = m_back;
    for (size_t i = 1; i < M; i++) cur_node = cur_node->prev;
    return cur_node->data;
  }
  
 private:
  struct node {
    node* next;
    node* prev;
    T data;

    node(node* a_next, node* a_prev, const T& a_data) :
      next(a_next), prev(a_prev), data(a_data) { }
  };

 private:
  node* m_front;
  node* m_back;
  size_t m_size;
};

int main() {
  uint32_t M;
  std::cin >> M;
  list<uint32_t> l;
  uint32_t item;
  while (std::cin >> item) l.push_back(item);
  if (M > l.size()) std::cout << "NIL\n";
  else std::cout << l.get_item_from_the_end(M) << std::endl;
}
