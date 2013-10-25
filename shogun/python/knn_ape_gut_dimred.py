#!/usr/bin/env python

from modshogun import *

fm_fname = '/home/iglesias/workspace/shogun/data/multiclass/fm_ape_gut.dat'
label_fname = '/home/iglesias/workspace/shogun/data/multiclass/label_ape_gut.dat'

# kNN classifier
knn = KNN()
knn.set_k(3)
euclidean_distance = EuclideanDistance()
knn.set_distance(euclidean_distance)

def evaluate(features, labels):
	# cross-validation and evaluation
	num_folds = 5
	splitting_strategy = StratifiedCrossValidationSplitting(labels, num_folds)
	evaluation = MulticlassAccuracy()

	cross_validation = CrossValidation(knn, features, labels, splitting_strategy, evaluation)
	cross_validation.set_autolock(False)
	cross_validation.set_num_runs(100)

	result = cross_validation.evaluate()
	result = CrossValidationResult.obtain_from_generic(result)
	return result.mean

features = RealFeatures(CSVFile(fm_fname))
labels = MulticlassLabels(CSVFile(label_fname))

print("Original:        %.4f" % evaluate(features, labels))

converter = TDistributedStochasticNeighborEmbedding()
converter.set_perplexity(25)
converter.set_target_dim(2)
print("TDSNE:           %.4f" % evaluate(converter.embed(features), labels))

converter = Isomap()
converter.set_k(20)
converter.set_target_dim(2)
print("Isomap:          %.4f" % evaluate(converter.embed(features), labels))

converter = DiffusionMaps()
converter.set_kernel(GaussianKernel(10, 10.0))
converter.set_t(10)
converter.set_target_dim(2)
print("Diffusion maps:  %.4f" % evaluate(converter.embed(features), labels))

converter = FactorAnalysis()
converter.set_target_dim(2)
print("Factor analysis: %.4f" % evaluate(converter.embed(features), labels))

# pca_features = RealFeatures(CSVFile(fm_fname))
# preprocessor = PCA()
# preprocessor.init(features)
# preprocessor.set_target_dim(2)
# preprocessor.apply_to_feature_matrix(pca_features)
# print("PCA:             " + str(evaluate(pca_features, labels)))
#
# kpca_features = RealFeatures(CSVFile(fm_fname))
# preprocessor = KernelPCA(GaussianKernel(kpca_features, kpca_features, 1.0))
# preprocessor.init(kpca_features)
# preprocessor.set_target_dim(2)
# preprocessor.apply_to_feature_matrix(kpca_features)
# print("Kernel PCA:      " + str(evaluate(kpca_features, labels)))

converter = KernelLocallyLinearEmbedding(LinearKernel())
converter.set_k(20)
converter.set_target_dim(2)
print("KLLE:            %.4f" % evaluate(converter.embed(features), labels))

