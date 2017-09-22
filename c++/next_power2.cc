#include <cassert>
#include <iostream>

// https://graphics.stanford.edu/~seander/bithacks.html#RoundUpPowerOf2
unsigned int next_power2(int n)
{
  assert(n >= 0);
  n--;
  n |= n >> 1;
  n |= n >> 2;
  n |= n >> 4;
  n |= n >> 8;
  n |= n >> 16;
  n++;
  n += (n == 0);

  return n;
}

unsigned int next_power2_loop(int n)
{
  assert(n >= 0);
  unsigned int i;
  for (i = 1; i < n; i <<= 1);
  return i;
}

int main(int argc, char* argv[])
{
  std::cout << next_power2_loop(atoi(argv[1])) << std::endl;
}
