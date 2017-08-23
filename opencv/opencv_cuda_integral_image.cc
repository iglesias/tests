/*
 * g++ -std=c++11 -Wall opencv_cuda_integral_image.cc -o opencv_cuda_integral_image -lopencv_core -lopencv_imgproc -lopencv_cudaarithm
 */

#include <algorithm>
#include <iostream>
#include <cstdint>

#include <opencv2/opencv.hpp>

int main()
{
  cv::Mat image = cv::Mat::ones(3, 3, CV_8UC1);

  std::random_device random_dev;
  std::mt19937 gen(random_dev());
  std::uniform_int_distribution<uchar> randi(0, UCHAR_MAX);

  auto assign_randi = [&gen, &randi](uchar& item) { item = randi(gen); };
  std::for_each(image.begin<uchar>(), image.end<uchar>(), assign_randi);

  std::cout << image << std::endl;

  cv::cuda::GpuMat gpu_image;
  gpu_image.upload(image);

  cv::cuda::GpuMat gpu_integral_image;
  cv::cuda::integral(gpu_image, gpu_integral_image);

  cv::Mat integral_image;
  gpu_integral_image.download(integral_image);

  std::cout << integral_image << std::endl;
}
