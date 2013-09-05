#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>

class RandomNumber {
  public:
    RandomNumber();

    friend std::ostream& operator<< (std::ostream& stream, RandomNumber& random_number);

    double Get() const { return x; }

  private:
    double x;
};

RandomNumber::RandomNumber() {
  x = 1.0*std::rand()/RAND_MAX;
}

std::ostream& operator<< (std::ostream& stream, RandomNumber& random_number) {
  stream << random_number.Get();
  return stream;
}

int main(int,char**) {
  std::srand(std::time(0));

  std::vector<RandomNumber> vrn;
  vrn.reserve(10);
  for (int i=0; i<10; ++i)
    vrn.push_back(RandomNumber());

  for (int i=0; i<(int)vrn.size(); ++i)
    std::cout << vrn[i] << std::endl;

  return 0;
}
