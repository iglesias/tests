#include <stdio.h>

char text[] = " pajarillo\n";

int main(int argc, char* argv[])
{
  // No error checking below.
  FILE* fd = fopen("dummy.txt", "a");
  fwrite(text, sizeof(text), 1, fd);
  fclose(fd);
  return 0;
}
