#include <iostream>
#include <map>
#include <stack>
#include <string>

std::map<char, char> CLOSING_TO_OPENING { {')', '('}, 
                                          {']', '['},
                                          {'}', '{'} };

bool is_opening(char c) {
  return c == '(' || c == '[' || c == '{'; 
}

bool is_closing(char c) {
  return c == ')' || c == ']' || c == '}'; 
}

int main() {
  std::string input;
  std::cin >> input;

  std::stack<char> stack;
  auto process_closing = [&stack](char closing) {
    // Opening character matching the given closing.
    char opening = CLOSING_TO_OPENING.find(closing)->second;
    if (stack.top() == opening) {
      stack.pop();
      return true;
    } else {
      return false;
    }
  };

  for (char c : input) {
    if (is_opening(c)) {
      stack.push(c);
    } else {
      if (!is_closing(c)) {
        std::cerr << "Invalid character " << c << " found in input.\n";
        std::exit(EXIT_FAILURE);
      }

      if (!process_closing(c)) {
        std::cout << "False\n";
        std::exit(EXIT_SUCCESS);
      }
    }
  }

  std::cout << (stack.size() ? "False\n" : "True\n");
}
