#!/usr/bin/python

from scipy import io

data_dict = io.loadmat('../data/NBData20_train_preprocessed.mat')

xt = data_dict['xt']
yt = data_dict['yt']

import numpy
from modshogun import RealFeatures,MulticlassLabels,LMNN,MSG_DEBUG

features = RealFeatures(xt.T)
labels = MulticlassLabels(numpy.squeeze(yt))

k = 6
lmnn = LMNN(features,labels,k)
lmnn.io.set_loglevel(MSG_DEBUG)
lmnn.set_diagonal(True)
lmnn.set_maxiter(10000)
lmnn.train(numpy.eye(features.get_num_features()))

