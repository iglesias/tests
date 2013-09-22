#!/usr/bin/python

from modshogun import CSVFile, RealFeatures, RescaleFeatures
from scipy.linalg import solve_triangular, cholesky, sqrtm, inv
import matplotlib.pyplot as pyplot
import numpy

# load wine features
features = RealFeatures(CSVFile('../data/fm_wine.dat'))

print('%d vectors with %d features.' % (features.get_num_vectors(), features.get_num_features()))
print('original features mean = ' + str(numpy.mean(features, axis=1)))

# rescale the features to [0,1]
feature_rescaling = RescaleFeatures()
feature_rescaling.init(features)
features.add_preprocessor(feature_rescaling)
features.apply_preprocessor()

print('mean after rescaling = ' + str(numpy.mean(features, axis=1)))

# remove mean from data
data = features.get_feature_matrix()
data = data.T
data-= numpy.mean(data, axis=0)
print numpy.mean(data, axis=0)

fig, axarr = pyplot.subplots(1,2)
axarr[0].matshow(numpy.cov(data.T))

#### whiten data

''' this method to whiten the data didn't really work out
L = cholesky(numpy.cov(data.T))
data = solve_triangular(L, data.T, lower=True).T
'''

# covariance matrix
M = numpy.cov(data.T)
Msqrt = sqrtm(M)
N = inv(Msqrt).real
datay = numpy.dot(N, data.T)

axarr[1].matshow(numpy.cov(datay))

whiten_features = RealFeatures(datay)
print('%d vectors with %d features.' % (whiten_features.get_num_vectors(), whiten_features.get_num_features()))

pyplot.show()
