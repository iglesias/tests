#include <Eigen/Dense>
#include <iostream>

int main(int,char**) {
	Eigen::Matrix2i A;
	A << 1,2,3,4;

	std::cout << "Initial matrix:\n" << A << std::endl;
	std::cout << "Its main diagonal:\n" << A.diagonal() << std::endl;
 	std::cout << "Its main diagonal as a diagonal matrix:\n" <<
			Eigen::Matrix2i(A.diagonal().asDiagonal()) << std::endl;

	return 0;
}
