#!/usr/bin/env python

from modshogun import KNN, RealFeatures, MulticlassLabels, EuclideanDistance, LMNN
import matplotlib.pyplot as pyplot
import numpy

COLS = ['r', 'b', 'g']

def sandwich_data(height=3,num_perclass=100):
	x = numpy.empty([0,2])
	y = numpy.empty(0)

	for h in xrange(height):
		mu = numpy.array([0,0.2*h])
		sigma = numpy.array([[2,0],[0,0]])
		xi = numpy.random.multivariate_normal(mu,sigma,num_perclass)
		xi[:,0] *= 10

		x = numpy.concatenate((x,xi))
		y = numpy.concatenate((y,numpy.array([h]*num_perclass)))

	return x,y

def plot_data(x,y,axis):
	for idx,val in enumerate(numpy.unique(y)):
		xi = x[y==val]
		axis.scatter(xi[:,0], xi[:,1], s=250, facecolors='none', edgecolors=COLS[idx])

def plot_neighborhood_graph(x, nn, axis):
	for i in xrange(x.shape[0]):
		xs = [x[i,0], x[nn[1,i], 0]]
		ys = [x[i,1], x[nn[1,i], 1]]
		axis.plot(xs, ys, COLS[int(y[i])])

figure, axarr = pyplot.subplots(1, 2)
# axis.set_ylim(-0.2,0.6)
x, y = sandwich_data(3, 20)

features = RealFeatures(x.T)
labels = MulticlassLabels(y)

print('%d vectors with %d features' % (features.get_num_vectors(), features.get_num_features()))
assert(features.get_num_vectors() == labels.get_num_labels())

distance = EuclideanDistance(features, features)
k = 2 
knn = KNN(k, distance, labels)

plot_data(x, y, axarr[0])
plot_neighborhood_graph(x, knn.nearest_neighbors(), axarr[0])

lmnn = LMNN(features, labels, k)
lmnn.set_maxiter(10000)
lmnn.train()
L = lmnn.get_linear_transform()
# x = numpy.dot(x, L.T)
knn.set_distance(lmnn.get_distance())

plot_data(x, y, axarr[1])
plot_neighborhood_graph(x, knn.nearest_neighbors(), axarr[1])


figure.text(.4, .95, '1-NN graph with Euclidean and LMNN distances')
pyplot.show()
