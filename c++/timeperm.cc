#include <iostream>
#include <algorithm>
#include <vector>
#include <chrono>
#include <random>
#include <climits>

#define FOR(i, a, b) for(auto i = (a); i < (b); ++i)
#define REP(i, n)    FOR(i, 0, n)
#define ALL(a)       (a).begin(), (a).end()

using namespace std;

int cost(const vector<vector<int>>& ar, const vector<int>& perm)
{
	int ans = ar[0][perm[0]];
	FOR(i, 1, perm.size()) ans += ar[perm[i-1]+1][perm[i]];
	return ans;
}

int main()
{
	random_device rd;
	mt19937 gen(rd());
	uniform_int_distribution<> dis(1, 40);

	vector<vector<int>> ar(11);
	REP(i, ar.size()) ar[i] = vector<int>(10, 0);

	REP(i, ar.size()) REP(j, ar[i].size())
		ar[i][j] = dis(gen);

	vector<int> perm(10);
	REP(i, perm.size()) perm[i] = i;

	int best_cost = INT_MAX;
	int it = 0;
	auto start = chrono::system_clock::now(); 
	do
	{
		best_cost = min(best_cost, cost(ar, perm));
		it++;
	} while(next_permutation(ALL(perm)));
	cout << chrono::duration<double>(chrono::system_clock::now()-start).count() << endl;

	cout << best_cost << ' ' << it << endl;

	return 0;
}
