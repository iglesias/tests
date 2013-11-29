import matplotlib.pyplot as pyplot
import pickle
import numpy

lmnn = pickle.load(open('lmnn_ape_gut_trained.p', 'rb'))
linear_transform = lmnn.get_linear_transform()
diagonal = numpy.diag(linear_transform)

title = '%d out of %d elements are non-zero' % (numpy.sum(linear_transform != 0), linear_transform.shape[0])

pyplot.stem(xrange(diagonal.size), diagonal)
pyplot.title(title)
pyplot.show()
