#!/usr/bin/env python

import matplotlib.pyplot as pyplot
import numpy

def sandwich_data(height=3,num_perclass=100):
	x = numpy.empty([0,2])
	y = numpy.empty(0)

	for h in xrange(height):
		mu = numpy.array([0,0.2*h])
		sigma = numpy.array([[0.1,0],[0,0]])
		xi = numpy.random.multivariate_normal(mu,sigma,num_perclass)

		x = numpy.concatenate((x,xi))
		y = numpy.concatenate((y,numpy.array([h]*num_perclass)))

	return x,y

def plot_data(x,y,axis):
	for idx,val in enumerate(numpy.unique(y)):
		xi = x[y==val]
		axis.plot(xi[:,0], xi[:,1], 'o', markersize=10)

figure,axis = pyplot.subplots(1,1)
axis.set_xlim(-2,2)
axis.set_ylim(-0.5,1)
x,y = sandwich_data()
plot_data(x,y,axis)
pyplot.show()
