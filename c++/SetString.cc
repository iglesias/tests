#include <set>
#include <string>
#include <iostream>

int main(int, char**)
{
	std::set<std::string> s;
	s.insert("AA");
	s.insert("AB");
	s.insert("AA");
	std::cout << s.size() << std::endl;
	return 0;
}
