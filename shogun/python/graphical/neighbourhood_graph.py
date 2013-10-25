#!/usr/bin/env python

from modshogun import KNN, RealFeatures, MulticlassLabels, EuclideanDistance, LMNN
import matplotlib.pyplot as pyplot
import numpy

COLS = ['r', 'b', 'g', 'm', 'k', 'y']

def sandwich_data():
	from numpy.random import normal

	# number of distinct classes
	nclasses = 6
	# number of points per class
	npoints = 9
	# distance between layers, the points of each class are in a layer
	dist = 0.7

	# memory pre-allocation
	x = numpy.zeros((nclasses*npoints, 2))
	y = numpy.zeros(nclasses*npoints)

	for i,j in zip(xrange(nclasses), xrange(-nclasses//2, nclasses//2+1)):
		for k, l in zip(xrange(npoints), xrange(-npoints//2, npoints//2+1)):
			x[i*npoints + k, :] = numpy.array([normal(l, 0.1), normal(dist*j, 0.1)])

		y[i*npoints:i*npoints+npoints] = i

	return x,y

def plot_data(x,y,axis):
	for idx,val in enumerate(numpy.unique(y)):
		xi = x[y==val]
		axis.scatter(xi[:,0], xi[:,1], s=50, facecolors='none', edgecolors=COLS[idx])

def plot_neighborhood_graph(x, nn, axis):
	for i in xrange(x.shape[0]):
		xs = [x[i,0], x[nn[1,i], 0]]
		ys = [x[i,1], x[nn[1,i], 1]]
		axis.plot(xs, ys, COLS[int(y[i])])

figure, axarr = pyplot.subplots(3, 1)
x, y = sandwich_data()

features = RealFeatures(x.T)
labels = MulticlassLabels(y)

print('%d vectors with %d features' % (features.get_num_vectors(), features.get_num_features()))
assert(features.get_num_vectors() == labels.get_num_labels())

distance = EuclideanDistance(features, features)
k = 2
knn = KNN(k, distance, labels)

plot_data(x, y, axarr[0])
plot_neighborhood_graph(x, knn.nearest_neighbors(), axarr[0])
axarr[0].set_aspect('equal')
axarr[0].set_xlim(-6, 4)
axarr[0].set_ylim(-3, 2)

lmnn = LMNN(features, labels, k)
lmnn.set_maxiter(10000)
lmnn.train()
L = lmnn.get_linear_transform()
knn.set_distance(lmnn.get_distance())

plot_data(x, y, axarr[1])
plot_neighborhood_graph(x, knn.nearest_neighbors(), axarr[1])
axarr[1].set_aspect('equal')
axarr[1].set_xlim(-6, 4)
axarr[1].set_ylim(-3, 2)

xL = numpy.dot(x, L.T) ## to see the data after the linear transformation
features = RealFeatures(xL.T)
distance = EuclideanDistance(features, features)
knn.set_distance(distance)

plot_data(xL, y, axarr[2])
plot_neighborhood_graph(xL, knn.nearest_neighbors(), axarr[2])
axarr[2].set_aspect('equal')
axarr[2].set_ylim(-3, 2)

pyplot.show()
