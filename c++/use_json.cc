#include <fstream>
#include <typeinfo>

#include "json.hpp"

using json = nlohmann::json;

int main() {
  {
    json j = {{"pi", 3.141},
              {"happy", true},
              {"name", "Niels"},
              {"nothing", nullptr},
              {"answer", {{"everything", 42}}},
              {"list", {1, 0, 2}},
              {"object", {{"currency", "USD"}, {"value", 42.99}}}};

    std::ofstream fout("example.json");
    fout << std::setw(4) << j << std::endl;
  }

  std::ifstream fin("example.json");
  json j;
  fin >> j;

  for (auto it = j.begin(); it != j.end(); ++it)
    std::cout << it.key() << " => " << it.value() << '\n';
  std::cout << '\n';

  std::cout << j["happy"] << "\n\n";

  std::for_each(j.begin(), j.end(),
                [](const auto &item) { std::cout << item << '\n'; });
}
