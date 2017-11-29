#include <algorithm>
#include <iostream>
#include <vector>

class timestamp
{
 public:
  timestamp(uint64_t t, bool is_start) : m_t(t), m_is_start(is_start) {}

  uint64_t t() const { return m_t; }

  bool is_start() const { return m_is_start; }

  bool operator<(const timestamp& other) const
  {
    if (m_t == other.m_t) return m_is_start;
    else                  return m_t < other.m_t;
  }

 private:
  uint64_t m_t;
  bool m_is_start;
};

int main()
{
  uint64_t num_timestamps;
  std::cin >> num_timestamps;

  std::vector<timestamp> timestamps;
  for (uint64_t i = 0; i < num_timestamps; i++)
  {
    uint64_t start, end;
    std::cin >> start >> end;
    timestamps.push_back(timestamp(start, true));
    timestamps.push_back(timestamp(end, false));
  }

  std::sort(timestamps.begin(), timestamps.end());

  uint64_t count = 0, max_count = 0;
  for (const auto& item : timestamps) {
    if (item.is_start()) {
      max_count = std::max(++count, max_count);
    } else {
      count--;
    }
  }

  std::cout << max_count << std::endl;
}
