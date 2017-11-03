#include <Eigen/Dense>
#include <iostream>

int main(int,char**) {
	Eigen::Matrix4d I = Eigen::Matrix4d::Identity();

	// Extract one block with all the columns and two rows.
	std::cout << I.block<2,4>(1,0) << std::endl << std::endl;
	// Extract one block with all the rows and two columns.
	std::cout << I.block<4,2>(0,1) << std::endl << std::endl;
	// Multiply the two blocks (typical matrix multiplication).
	std::cout << I.block<2,4>(1,0)*I.block<4,2>(0,1) << std::endl;

	return 0;
}
