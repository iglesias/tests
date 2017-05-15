// Proof of concept interface for Shogun based on unique_ptr.

#include <Eigen/Dense>
#include <memory>
#include <string>

class Features {
 public:
  Features(size_t num_features, size_t num_vectors) :
    num_vectors(num_vectors), m_featmat(num_features, num_vectors) {}

 public:
  size_t num_vectors;

 private:
  Eigen::MatrixXd m_featmat;
};

class Labels {
 public:
  Labels(size_t num_labels) : m_labvec(num_labels) {}

 private:
  Eigen::VectorXd m_labvec;
};

class Clustering {
 public:
  Clustering(Features* features) : m_features(features) {}

  // it should be pure virtual, here no only to avoid boilerplate.
  virtual std::unique_ptr<Labels> cluster()
  {
    return std::make_unique<Labels>(m_features->num_vectors);
  }
 
 protected:
  Features* m_features;
};

class KMeans : public Clustering {
 public:
  KMeans(Features* features) : Clustering(features) {}
};

class GMM : public Clustering {
 public:
  GMM(Features* features) : Clustering(features) {}
};

std::unique_ptr<Features> load_features(std::string file_name) {
  return std::make_unique<Features>(1024, 1e4);
}

int main()
{
  std::unique_ptr<Features> features = load_features("file_name");
  auto kmeans = KMeans(features.get());
  auto gmm = GMM(features.get());
  std::unique_ptr<Labels> kmeans_result = kmeans.cluster();
  std::unique_ptr<Labels> gmm_result = gmm.cluster();
}
