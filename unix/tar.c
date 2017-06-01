#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>

char buf[] = "Hola\n";

int main(int argc, char* argv[])
{
  int fd = open("tmp.txt", O_CREAT | O_WRONLY);
  usleep(2e6);
  write(fd, buf, sizeof(buf));
  usleep(2e6);
  close(fd);
  unlink("tmp.txt");
  return 0;
}
