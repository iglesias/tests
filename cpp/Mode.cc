#include <iostream>
#include <unordered_map>
#include <vector>

int GetMode(const std::vector<int>& vi)
{
  if (vi.size() == 0)
  {
    std::cerr << "No mode for empty array.\n";
    std::exit(1);
  }

  std::unordered_map<int, int> dict;
  int mode = vi[0];
  int max_freq = 1;

  for (int n : vi)
  {
    if (dict.find(n) == dict.end())
    {
      dict.insert({n, 1});
    }
    else
    {
      dict[n]++;
      if (dict[n] > max_freq)
      {
        max_freq = dict[n];
        mode = n;
      }
    }
  }

  return mode;
}

int main()
{
  std::vector<int> vi = {1, 2, 2, 3, 4, 0};
  std::cout << GetMode(vi) << std::endl;
}
