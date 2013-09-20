#!/usr/bin/env python

from modshogun import *

# load metagenomics ape gut data set
features = RealFeatures(CSVFile('../data/fm_ape_gut.txt'))
labels = MulticlassLabels(CSVFile('../data/label_ape_gut.txt'))

print('Number of examples = %d, number of features = %d.' % (features.get_num_vectors(), features.get_num_features()))

# kNN classifier
knn = KNN()
knn.set_k(3)
euclidean_distance = EuclideanDistance()
knn.set_distance(euclidean_distance)

# splitting strategy for 5-fold cross-validation
# we use stratetified to maintain
splitting_strategy = StratifiedCrossValidationSplitting(labels, 5)

# evaluation method
evaluation = MulticlassAccuracy()

# prepare cross-validation instance
cross_validation = CrossValidation(knn, features, labels, splitting_strategy, evaluation)
# locking is not supported for kNN, deactivate it to avoid warning
cross_validation.set_autolock(False)
cross_validation.set_num_runs(100)

# perform cross-validation and show results
result = cross_validation.evaluate()
result = CrossValidationResult.obtain_from_generic(result)
print (result.mean)
