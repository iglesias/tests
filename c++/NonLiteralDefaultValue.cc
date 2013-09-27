#include <vector>
#include <iostream>

// This doesn't compile
template <class T>
void print(const std::vector<T> v, int i=v.size())
{
	std::cout << "v.size() = " << v.size() << " i = " << i << std::endl;
}

int main(int, char**)
{
	print(std::vector<int>(), 5);
	return 0;
}
