#include <boost/random/normal_distribution.hpp>
#include <boost/random/mersenne_twister.hpp>
#include <boost/accumulators/accumulators.hpp>
#include <boost/accumulators/statistics/stats.hpp>
#include <boost/accumulators/statistics/mean.hpp>
#include <boost/accumulators/statistics/moment.hpp>

using namespace boost::accumulators;

int main(int,char**) {
  boost::random::mt19937 rng;
  boost::random::normal_distribution<> standard_normal(0,1);

  int num_samples;
  std::cout << "How many samples of the normal (0,1) do you want to simulate? ";
  std::cin >> num_samples;

  accumulator_set<double, stats<tag::mean, tag::moment<2> > > acc;
  for (int i=0; i<num_samples; ++i)
    acc(standard_normal(rng));

  std::cout << "Sample mean:     " << mean(acc) << std::endl;
  std::cout << "Sample variance: " << moment<2>(acc) << std::endl;

  return 0;
}
