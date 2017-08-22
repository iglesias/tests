/*
 * g++ -std=c++11 -Wall opencv_integral_image.cc -o opencv_integral_image -lopencv_core -lopencv_imgproc
 */

#include <algorithm>
#include <iostream>
#include <random>

#include <opencv2/opencv.hpp>

int main()
{
  cv::Mat image(3, 5, CV_32FC1);

  std::random_device random_dev;
  std::mt19937 gen(random_dev());
  std::uniform_real_distribution<float> rand;

  auto assign_rand = [&rand, &gen](float& item) { item = rand(gen); };
  std::for_each(image.begin<float>(), image.end<float>(), assign_rand);
  std::cout << image << std::endl;

  cv::Mat integral_image;
  cv::integral(image, integral_image);
  std::cout << integral_image << std::endl;
}
