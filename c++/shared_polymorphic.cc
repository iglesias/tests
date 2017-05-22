#include <iostream>
#include <memory>
#include <typeinfo>

class Base {
 public:
  virtual void generic_method(const std::shared_ptr<Base>& other) const
  {
    std::cout << typeid(this).name() << std::endl;
    std::cout << typeid(*this).name() << std::endl;
    std::cout << typeid(*other).name() << std::endl;
  }
};

class Derived1 : public Base {
};

class Derived2 : public Base {
};

int main()
{
  auto d1 = std::make_shared<Derived1>();
  auto d2 = std::make_shared<Derived2>();
  d1->generic_method(d2);
  d2->generic_method(d1);
  d2->generic_method(d2);
}
