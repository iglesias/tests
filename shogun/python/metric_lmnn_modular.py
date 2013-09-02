#!/usr/bin/python

import numpy

wine_data = numpy.loadtxt('../data/wine.data', delimiter=',')

# separate labels and features from the data
# the labels appear in the first column
labels = wine_data[:,0].astype(numpy.float64)
features = wine_data[:,1:]

print('There are %d vectors with %d features from %d different classes.' % \
		(features.shape[0], features.shape[1], numpy.unique(labels).shape[0]))

# feature normalization
features = (features-features.min(axis=0)) / (features.max(axis=0)-features.min(axis=0))
assert(features.min()>=0.0 and features.max()<=1.0)

from modshogun import RealFeatures, MulticlassLabels, MulticlassAccuracy, LMNN, KNN

accuracies = []
evaluator = MulticlassAccuracy()
n = 10
k = 5

for i in xrange(n):

	print('Pass #%d' % i)

	# select a ratio of the number of features for training and the rest for testing
	ratio = 0.7
	randperm = numpy.random.permutation(range(features.shape[0]))
	pivot = numpy.floor(ratio*randperm.shape[0])
	train_idxs = randperm[:pivot]
	test_idxs = randperm[pivot:]

	print('Using %d vectors for training' % train_idxs.shape[0])

	train_features = features[train_idxs,:]
	train_labels = labels[train_idxs]

	test_features = features[test_idxs,:]
	test_labels = labels[test_idxs]

	# wrap features and labels into Shogun objects

	train_labels = MulticlassLabels(train_labels)
	train_features = RealFeatures(train_features.T)

	test_labels = MulticlassLabels(test_labels)
	test_features = RealFeatures(test_features.T)

	# train LMNN

	lmnn = LMNN(train_features,train_labels,k)
	lmnn.set_maxiter(1000)
	lmnn.set_correction(15)
# 	lmnn.io.set_loglevel(MSG_DEBUG)

	init_transform = numpy.eye(train_features.get_num_features())
	lmnn.train(init_transform)

	distance = lmnn.get_distance()
	lmnnknn = KNN(k,distance,train_labels)
	lmnnknn.train()
	test_output = lmnnknn.apply(test_features)
	accuracies.append(evaluator.evaluate(test_output,test_labels))

print accuracies
print("Mean accuracy after %d runs is equal to %.2f" % (n,numpy.mean(accuracies)))
