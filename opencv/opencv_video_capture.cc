/*
 * g++ -std=c++11 -Wall -g opencv_video_capture.cc -o opencv_video_capture -lopencv_core -lopencv_videoio
 */

#include <chrono>
#include <iostream>
#include <string>

#include <opencv2/opencv.hpp>

int main()
{
  std::string video_path = std::string("path_to_video");
  auto video_capture = cv::VideoCapture(video_path);
  std::cout << video_capture.get(CV_CAP_PROP_FPS) << std::endl;

  if (!video_capture.isOpened()) {
    std::cerr << "The VideoCapture is not opened\n";
    return 1;
  }

  for (int i = 0; i < 10; i++) {
    cv::Mat frame;
    auto start = std::chrono::system_clock::now();
    if (!video_capture.grab())
      std::cerr << "The frame could not be read form the VideoCapture\n";

    std::cout << std::chrono::duration<double>(std::chrono::system_clock::now()
                                               -start).count() << std::endl;
    start = std::chrono::system_clock::now();

    video_capture.retrieve(frame);
    std::cout << std::chrono::duration<double>(std::chrono::system_clock::now()
                                               -start).count() << std::endl;
  }
}
