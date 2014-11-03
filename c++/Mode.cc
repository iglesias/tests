#include <iostream>
#include <unordered_map>
#include <utility>
#include <vector>

int GetMode(const std::vector<int>& vi)
{
	std::unordered_map<int, int> dict;

	for (unsigned int i = 0; i < vi.size(); i++)
	{
		if (dict.find(vi[i]) == dict.end()) dict.insert(std::make_pair(vi[i], 1));
		else
		{
			int tmp = dict.find(vi[i])->second;
			dict.erase(vi[i]);
			dict.insert(std::make_pair(vi[i], tmp+1));
		}
	}

	auto mode_it = dict.begin();
	for (auto it = next(mode_it); it != dict.end(); it++)
		if (it->second > mode_it->second) mode_it = it;

	return mode_it->first;
}

int main()
{
	std::vector<int> vi = {1, 2, 2, 3, 4, 0};
	std::cout << GetMode(vi) << std::endl;
	return 0;
}
