/** This stops with a segmentation fault when global is roughly equal
 * to half a million. Although this value probably depends on the hardware
 * at hand. Also, if optimizations are enabled at compilation (with -O) it seems
 * that the compiler optimizes out the recursive call and just executes
 * the print statement.
 */

#include <iostream>

using namespace std;

long long global;

void recurse()
{
  cout << ++global << endl;
  recurse();
}

int main()
{
  recurse();
}
