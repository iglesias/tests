#!/usr/bin/python

import matplotlib.pyplot as pyplot
import pickle

from modshogun import CSVFile, RealFeatures, MulticlassLabels

features_file = '../data/fm_ape_gut.txt'
labels_file = '../data/label_ape_gut.txt'

features = RealFeatures(CSVFile(features_file))
labels = MulticlassLabels(CSVFile(labels_file))


def plot_data(x,y):

	pyplot.scatter(x[0,y==0], x[1,y==0], color='green')
	pyplot.scatter(x[0,y==1], x[1,y==1], color='red')
	pyplot.scatter(x[0,y==2], x[1,y==2], color='blue')

def visualize_tdsne(features,labels):
	from modshogun import TDistributedStochasticNeighborEmbedding

	converter = TDistributedStochasticNeighborEmbedding()
	converter.set_target_dim(2)
	converter.set_perplexity(25)

	embedding = converter.embed(features)

	plot_data(embedding.get_feature_matrix(),labels.get_labels())
	pyplot.show()

def visualize_spe(features,labels):
	from modshogun import StochasticProximityEmbedding, SPE_GLOBAL

	converter = StochasticProximityEmbedding()
	converter.set_strategy(SPE_GLOBAL)
	converter.set_k(10)
	converter.set_target_dim(2)
	converter.set_nupdates(40);

	embedding = converter.embed(features)

	plot_data(embedding.get_feature_matrix(),labels.get_labels())
	pyplot.show()

def diagonal_lmnn(features,labels,k=3,max_iter=10000):

	from modshogun import LMNN, MSG_DEBUG
	import numpy

	lmnn = LMNN(features,labels,k)
	lmnn.io.set_loglevel(MSG_DEBUG)
	lmnn.set_diagonal(True)
	lmnn.set_maxiter(max_iter)
	lmnn.train(numpy.eye(features.get_num_features()))

	pickle.dump(lmnn, open('lmnn_ape_gut_trained.p', 'wb'))

	linear_transform = lmnn.get_linear_transform()
	diagonal = numpy.diag(linear_transform)
	pyplot.stem(xrange(diagonal.size), diagonal)
	pyplot.show()

diagonal_lmnn(features,labels)
