#!/usr/bin/python

from modshogun import *
import scipy.linalg as linalg
import numpy
import matplotlib.pyplot as pyplot

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
# save value for final bar chart
euclidean_means = numpy.zeros(3)
euclidean_means[0] = result.mean

print ('kNN accuracy with Euclidean distance: %.4f.' % result.mean)

lmnn = LMNN(features, labels, k)
lmnn.set_maxiter(5000)
# lmnn.io.set_loglevel(MSG_DEBUG)
lmnn.train()

# evaluate, this time using the distance found by LMNN
knn.set_distance(lmnn.get_distance())
result = cross_validation.evaluate()
result = CrossValidationResult.obtain_from_generic(result)
# save value for final bar chart
lmnn_means = numpy.zeros(3)
lmnn_means[0] = result.mean

print ('kNN accuracy with distance found by LMNN: %.4f.' % result.mean)

### same experiment, but rescaling the features this time to produce a fair comparison
### for kNN

# rescale features so that all vary within [0,1]
preprocessor = RescaleFeatures()
preprocessor.init(features)
features.add_preprocessor(preprocessor)
features.apply_preprocessor()

feature_matrix = features.get_feature_matrix()
assert(feature_matrix.min()>=0.0 and feature_matrix.max()<=1.0)

knn.set_distance(EuclideanDistance())
result = cross_validation.evaluate()
result = CrossValidationResult.obtain_from_generic(result)
euclidean_means[1] = result.mean

print ('kNN accuracy with Euclidean distance after rescaling: %.4f.' % result.mean)

lmnn.train()
knn.set_distance(lmnn.get_distance())
result = cross_validation.evaluate()
result = CrossValidationResult.obtain_from_generic(result)
lmnn_means[1] = result.mean

print ('kNN accuracy with distance found by LMNN after rescaling: %.4f.' % result.mean)

### same experiment, whith data whitening

## whiten data as explanined in http://en.wikipedia.org/wiki/Whitening_transformation
data = features.get_feature_matrix() # shorthand for the feature matrix -- copies data
# remove mean for each feature
data = data.T
data-= numpy.mean(data, axis=0)
# compute the square root of the covariance matrix
M = linalg.sqrtm(numpy.cov(data.T))
# matrix inverse
N = linalg.inv(M).real
# apply whitening transform
white_data = numpy.dot(N, data.T)
white_features = RealFeatures(white_data)

# check that the new covariance is equal to the identity matrix
# pyplot.matshow(numpy.cov(white_features))
# pyplot.colorbar()
# pyplot.show()

# evaluate kNN and LMNN
features = white_features

knn.set_distance(EuclideanDistance())
result = cross_validation.evaluate()
result = CrossValidationResult.obtain_from_generic(result)
euclidean_means[2] = result.mean

print ('kNN accuracy with Euclidean distance after whitening: %.4f.' % result.mean)

lmnn.train()
knn.set_distance(lmnn.get_distance())
result = cross_validation.evaluate()
result = CrossValidationResult.obtain_from_generic(result)
lmnn_means[2] = result.mean

print ('kNN accuracy with distance found by LMNN after whitening: %.4f.' % result.mean)

# bar chart (adapted from http://matplotlib.org/examples/api/barchart_demo.html)
assert(euclidean_means.shape[0] == lmnn_means.shape[0])
N = euclidean_means.shape[0]
# the x locations for the groups
ind = 0.5*numpy.arange(N)
# the width of the bars
width = 0.15
figure, axes = pyplot.subplots()

euclidean_rects = axes.bar(ind, euclidean_means, width, color='y')
lmnn_rects = axes.bar(ind+width, lmnn_means, width, color='r')

# add information to the chart
axes.set_ylabel('Accuracies')
axes.set_ylim(top=1.3)
axes.set_title('kNN accuracy by distance and feature preprocessing')
axes.set_xticks(ind+width)
axes.set_xticklabels(('Raw', 'Rescaling', 'Whitening'))
axes.legend((euclidean_rects[0], lmnn_rects[0]), ('Euclidean', 'LMNN'), loc='upper right')

def autolabel(rects):
	# attach text labels to bars
	for rect in rects:
		height = rect.get_height()
		axes.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%.3f'%height,
				ha='center', va='bottom')

autolabel(euclidean_rects)
autolabel(lmnn_rects)

pyplot.show()
