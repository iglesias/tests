#!/usr/bin/python

from modshogun import *

# load wine data set
features = RealFeatures(CSVFile('../data/fm_wine.dat'))
labels =  MulticlassLabels(CSVFile('../data/label_wine.dat'))

assert(features.get_num_vectors() == labels.get_num_labels())

print('There are %d vectors with %d features from %d different classes.' % \
	(features.get_num_vectors(), features.get_num_features(), labels.get_num_classes()))

# kNN classifier
k = 5
knn = KNN()
knn.set_k(k)
knn.set_distance(EuclideanDistance())

# evaluate classification accuracy using cross-validation
splitting_strategy = StratifiedCrossValidationSplitting(labels, 5)
evaluation = MulticlassAccuracy()
cross_validation = CrossValidation(knn, features, labels, splitting_strategy, evaluation)
cross_validation.set_autolock(False)
cross_validation.set_num_runs(200)
result = cross_validation.evaluate()
result = CrossValidationResult.obtain_from_generic(result)

print ('kNN accuracy with Euclidean distance: %.4f.' % result.mean)

lmnn = LMNN(features, labels, k)
lmnn.set_maxiter(5000)
# lmnn.io.set_loglevel(MSG_DEBUG)
lmnn.train()

# evaluate, this time using the distance found by LMNN
knn.set_distance(lmnn.get_distance())
result = cross_validation.evaluate()
result = CrossValidationResult.obtain_from_generic(result)

print ('kNN accuracy with distance found by LMNN: %.4f.' % result.mean)

### same experiment, but rescaling the features this time to produce a fair comparison
### for kNN

# rescale features so that the all vary within [0,1]
preprocessor = RescaleFeatures()
preprocessor.init(features)
features.add_preprocessor(preprocessor)
features.apply_preprocessor()

feature_matrix = features.get_feature_matrix()
assert(feature_matrix.min()>=0.0 and feature_matrix.max()<=1.0)

knn.set_distance(EuclideanDistance())
result = cross_validation.evaluate()
result = CrossValidationResult.obtain_from_generic(result)

print ('kNN accuracy with Euclidean distance after rescaling: %.4f.' % result.mean)

lmnn.train()
knn.set_distance(lmnn.get_distance())
result = cross_validation.evaluate()
result = CrossValidationResult.obtain_from_generic(result)

print ('kNN accuracy with distance found by LMNN after rescaling: %.4f.' % result.mean)
