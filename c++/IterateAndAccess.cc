/* Investigating what was wrong with https://github.com/shogun-toolbox/shogun/pull/1478 */

#include <iostream>
#include <vector>

int main(int, char**) {
	int vi[] = {2,4,6,8,10};

	for (int i=0, j=vi[0]; i<5; i++, j=vi[i])
		std::cout << i << ", " << j << std::endl; 

	return 0;
}
