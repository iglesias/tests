#include <Eigen/Dense>
#include <iostream>

int main(int,char**) {
	Eigen::VectorXd zero;
	zero.resize(5);
	zero.setZero();

	Eigen::VectorXd v(5);
	v << -1,2,-3,4,-7;

	std::cout << v.array().max(zero.array()) << std::endl << std::endl;

	Eigen::VectorXd x = v.array().max(zero.array()).sqrt();
	std::cout << x << std::endl;

	return 0;
}
