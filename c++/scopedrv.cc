/**
 * The output is
 * 1
 * 0
 * tested with clang 3.0-6ubuntu3 and gcc 4.6.4-1ubuntu1
 */

#include <iostream>

class Dummy
{
	public:
		Dummy() { num_instances++; }
		~Dummy() { num_instances--; };
		static void PrintNumInstances() { std::cout << num_instances << std::endl; }

	public:
		static int num_instances;
};

int Dummy::num_instances = 0;

Dummy ReturnDummy()
{
	Dummy dummy;
	Dummy::PrintNumInstances();
	return dummy;
}

int main()
{
	ReturnDummy();
	Dummy::PrintNumInstances();
	return 0;
}
