/*
 * mapconst.cc
 * g++ -g -std=c++11 -Wall -I /usr/include/eigen3 mapconst.cc -o mapconst -lshogun
 */ 

#include <iostream>

#include <Eigen/Dense>
#include <shogun/base/init.h>
#include <shogun/lib/SGMatrix.h>

using namespace shogun;
using namespace Eigen;

int num_rows=3, num_cols=2;

void f(const SGMatrix<float64_t>& feat_mat)
{
  Map<MatrixXd> fmatrix(feat_mat.matrix, num_rows, num_cols);
  std::cout << fmatrix.transpose() << std::endl;
  std::cout << fmatrix << std::endl;
}

int main()
{
  init_shogun_with_defaults();

  SGMatrix<float64_t> feat_mat(num_rows, num_cols);
  // 1st row
  feat_mat(0,0)=1;
  feat_mat(0,1)=2;
  // 2nd row
  feat_mat(1,0)=3;
  feat_mat(1,1)=4;
  // 3rd row
  feat_mat(2,0)=5;
  feat_mat(2,1)=6;

  feat_mat.display_matrix();
  f(feat_mat);
  feat_mat.display_matrix();

  exit_shogun();
}
