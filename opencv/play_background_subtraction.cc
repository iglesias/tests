/* 
 * play_background_subtraction.cc
 * 
 * g++ -std=c++11 -Wall -g play_background_subtraction.cc -lopencv_core -lopencv_cudabgsegm -lopencv_imgcodecs -o play_background_subtraction
 */

#include <ctime>
#include <cstdlib>
#include <iostream>
#include <string>

#include <opencv2/cudabgsegm.hpp>
#include <opencv2/opencv.hpp>

unsigned char rand_uchar()
{
  return static_cast<unsigned char>(std::rand()%100);
}

cv::Mat random_frame()
{
  std::srand(std::time(0));

  size_t num_rows = 3, num_cols = 3;
  cv::Mat frame(num_rows, num_cols, CV_8UC3);
  for (size_t i = 0; i < num_rows; i++)
    for (size_t j = 0; j < num_cols; j++)
      frame.at<cv::Vec3b>(i,j) = {rand_uchar(), rand_uchar(), rand_uchar()};

  std::cout << frame << std::endl;
  return frame;
}

cv::Mat load_frame(const std::string& fname)
{
  cv::Mat frame = cv::imread(fname);
  if (frame.data == nullptr) {
    std::cerr << "Input frame could not be read\n.";
    std::exit(EXIT_FAILURE);
  }

  return frame;
}

cv::Mat zero_frame()
{
  return cv::Mat(1, 1, CV_8UC3, cv::Scalar(0));
}

int main()
{
  cv::cuda::GpuMat gpu_frame(random_frame());

  auto background_subtractor = cv::cuda::createBackgroundSubtractorMOG2();

  cv::cuda::GpuMat output;
  background_subtractor->apply(gpu_frame, output);
}
