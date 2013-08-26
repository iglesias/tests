#include <Eigen/Dense>
#include <iostream>

int main(int,char**) {
	Eigen::MatrixXd A(3,3);
	A << 1,-2,3,-4,5,-6,7,-8,9;
	Eigen::MatrixXd O(3,3);
	O.setZero();
	Eigen::MatrixXd B = A.array().max(O.array());

	std::cout << A << std::endl << std::endl;
	std::cout << B << std::endl;

	return 0;
}
