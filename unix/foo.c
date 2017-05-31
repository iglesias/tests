#include <stdio.h>
#include <unistd.h>

char buffer[1024];

int main(int argc, char* argv[])
{
  // No error checking below.
  FILE* fd = fopen("dummy.txt", "r");
  usleep(3e6);
  fread(buffer, 1024, 1, fd);
  printf("%s", buffer);
  fclose(fd);
  return 0;
}
