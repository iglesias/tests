#include <shogun/base/init.h>
#include <shogun/features/DenseFeatures.h>
#include <shogun/distance/EuclideanDistance.h>
#include <iostream>

using namespace shogun;
using namespace std;

void print_message(FILE* target, const char* str)
{
        fprintf(target, "%s", str);
}

int main(int argc, char **argv)
{
    init_shogun(&print_message, &print_message, &print_message);
    int32_t dim_features = 2;
    SGMatrix<float64_t> data(dim_features, 4);
    float64_t t[8] = {0,0,0,10,1,10,1,0};
    data.matrix = t;
    SGMatrix<float64_t>::display_matrix(data.matrix, 2, 4, "matrix");

    float64_t mus_start[4] = {0,5,1,5};

    CDenseFeatures<float64_t>* features=new CDenseFeatures<float64_t> ();
    features->set_feature_matrix(data);
    SG_REF(features);

    CEuclideanDistance* distance=new CEuclideanDistance(features, features);
    CDenseFeatures<float64_t>* rhs_mus = new CDenseFeatures<float64_t>(0);   
    CFeatures* rhs_cache = distance->replace_rhs(rhs_mus);

    rhs_mus->copy_feature_matrix(SGMatrix<float64_t>(mus_start,2,2,false)); 
    exit_shogun();
    return 0;
}
