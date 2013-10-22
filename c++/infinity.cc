#include <limits>
#include <iostream>

using namespace std;

int main()
{
  double inf = numeric_limits<double>::infinity();
  cout << "Infinity is displayed as " << inf << endl;
  double test = inf+5;
  cout << "Does it overflow? " << test << endl;
  test = inf+inf;
  cout << "Does it overflow? " << test << endl;
  cout << "Testing equality: " << (inf-10 == numeric_limits<double>::infinity()) << endl;

  return 0;
}
