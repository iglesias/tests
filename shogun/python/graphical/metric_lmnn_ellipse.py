#!/usr/bin/python

import numpy
import matplotlib.pyplot as pyplot

FIGURE,AXIS = pyplot.subplots(1,1)

def plot_data(features,labels):
	# separate features according to their class
	X0, X1, X2 = features[labels==0], features[labels==1], features[labels==2]

	# class 0 data
	AXIS.plot(X0[:,0], X0[:,1], 'o', color='green', markersize=12)
	# class 1 data
	AXIS.plot(X1[:,0], X1[:,1], 'o', color='red', markersize=12)
	# class 2 data
	AXIS.plot(X2[:,0], X2[:,1], 'o', color='blue', markersize=12)

def plot_covariance_ellipse(covariance):
	import matplotlib.patches as patches
	import scipy.linalg as linalg

	# the ellipse is centered at (0,0)
	mean = numpy.array([0,0])

	# eigenvalue decomposition of the covariance (w eigenvalues, v eigenvectors) keeping
	# only the real part
	w, v = linalg.eigh(covariance)
	# normalize the eigenvector corresponding to the largest eigenvalue
	u = v[0]/linalg.norm(v[0])
	# angle in radians degrees
	angle = 180.0/numpy.pi*numpy.arctan(u[1]/u[0])
	# fill Gaussian ellipse at 2 standard deviation
	ellipse = patches.Ellipse(mean, 2*w[0]**0.5, 2*w[1]**0.5, 180+angle,
			color='green', alpha=0.4)

	# plot the ellipse
	AXIS.add_artist(ellipse)
	AXIS.set_xlim(-1.5,1.5)
	AXIS.set_ylim(-1.5,1.5)
	AXIS.set_aspect('equal')

	pyplot.show()

from shogun.Features import RealFeatures, MulticlassLabels
from shogun.Metric import LMNN


# input features and labels
features = numpy.array([[0,0],[-1,0.1],[0.3,-0.05],[0.7,0.3],[-0.2,-0.6],
						[-0.15,-0.63],[-0.25,0.55],[-0.28,0.67]])
labels = numpy.array([0,0,0,0,1,1,2,2], dtype=numpy.float64)

plot_data(features,labels)

# wrap them into Shogun objects
features = RealFeatures(features.T)
labels = MulticlassLabels(labels)

# train LMNN
# number of target neighbours per example
k = 1
lmnn = LMNN(features,labels,k)
lmnn.set_maxiter(1000)
lmnn.set_correction(15)
lmnn.train()

L = lmnn.get_linear_transform()
M = numpy.matrix(numpy.dot(L.T,L))

plot_covariance_ellipse(M.I)
#plot_covariance_ellipse(numpy.eye(2))
