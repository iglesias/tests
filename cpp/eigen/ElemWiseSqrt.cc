#include <Eigen/Dense>
#include <iostream>

int main(int,char**) {
	Eigen::MatrixXd A(3,3);
	A << 1,2,3,4,5,6,7,8,9;

	std::cout << A << std::endl << std::endl;
	A = A.array().sqrt();
	std::cout << A << std::endl;

	return 0;
}
