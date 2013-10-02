#include <iostream>
#include <set>
#include <iterator>

int main()
{
	std::multiset<int> ms;
	int N = 10;
	for (int i = 0; i < N; i++)
	{
		ms.insert(i);
		ms.insert(i);
	}

	int d = std::distance(ms.upper_bound(8), ms.end());
	std::cout << d << std::endl;

	return 0;
}
