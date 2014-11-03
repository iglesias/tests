#include "LinkedList.hpp"
#include <list>

int main()
{
	LinkedList<int> list;
	//std::list<int> list;

	for (int i=0; i<1e8; i++)
		list.push_back(i);

	return 0;
}
