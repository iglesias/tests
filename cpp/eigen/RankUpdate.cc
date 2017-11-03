#include <Eigen/Dense>
#include <iostream>
#include <chrono>

void selfouterProduct(Eigen::MatrixXd& A, const Eigen::VectorXd& v) {
  assert(A.rows() == A.cols() && A.rows() == v.size());

  for (int i = 0; i < v.size(); ++i)
    for (int j = i; j < v.size(); ++j) {
      A(i, j) += v(i)*v(j); 
    }
}

int main(int argc, char** argv) {
  int N = 10000;
  Eigen::VectorXd v(N);
  for (int i = 0; i < N; ++i)
    v(i) = i+1;

  auto t1 = std::chrono::high_resolution_clock::now();
  Eigen::MatrixXd outer_product = v*v.transpose();
  auto t2 = std::chrono::high_resolution_clock::now();
//   std::cout << outer_product << std::endl << std::endl;
  std::cout << std::chrono::duration_cast<std::chrono::milliseconds>(t2-t1).count() << " (ms).\n";

  Eigen::MatrixXd A(N,N);
  A.setZero();
  // m = m + v*v.transpose()
  auto t3 = std::chrono::high_resolution_clock::now();
  A.selfadjointView<Eigen::Upper>().rankUpdate(v);
//   A.triangularView<Eigen::StrictlyLower>() = A.transpose();
  auto t4 = std::chrono::high_resolution_clock::now();
//   std::cout << A << std::endl << std::endl;
  std::cout << std::chrono::duration_cast<std::chrono::milliseconds>(t4-t3).count() << " (ms).\n";

  Eigen::MatrixXd B(N,N);
  B.setZero();
  auto t5 = std::chrono::high_resolution_clock::now();
  selfouterProduct(B, v);
//   B.triangularView<Eigen::StrictlyLower>() = B.transpose();
  auto t6 = std::chrono::high_resolution_clock::now();
//   std::cout << B << std::endl;
  std::cout << std::chrono::duration_cast<std::chrono::milliseconds>(t6-t5).count() << " (ms).\n";

  return 0;
}
