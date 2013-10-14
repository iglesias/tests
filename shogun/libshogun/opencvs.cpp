#include <shogun/io/CSVFile.h>
#include <fcntl.h>

int main(int, char**)
{
	shogun::init_shogun_with_defaults();

	int fd = open("/home/iglesias/workspace/shogun-octave/data/toy/fm_train_multiclass_digits.dat", O_RDONLY);
	shogun::CCSVFile csvfile(fd);

	shogun::exit_shogun();

	return 0;
}
