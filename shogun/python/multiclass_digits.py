#!/usr/bin/env python

import scipy
from scipy import io

data_dict = scipy.io.loadmat('digits.mat', struct_as_record=False)
parameter_list=[[data_dict]]

def load_data(num_train_samples=7291, m_data_dict=data_dict):
	from modshogun import RealFeatures, MulticlassLabels
	import numpy

	train_vec = m_data_dict['yTr'][0][:num_train_samples].astype(numpy.float64)
	train_labels = MulticlassLabels(train_vec)
	test_vec = m_data_dict['yTe'][0].astype(numpy.float64)
 	test_labels = MulticlassLabels(test_vec)
	print "#train_labels = " + str(train_labels.get_num_labels())
	print "#test_labels  = " + str(test_labels.get_num_labels())

	train_mat = m_data_dict['xTr'][:,:num_train_samples].astype(numpy.float64)
	train_features = RealFeatures(train_mat)
	test_mat = m_data_dict['xTe'].astype(numpy.float64)
	test_features = RealFeatures(test_mat)
	print "#train_vectors = " + str(train_features.get_num_vectors())
	print "#test_vectors  = " + str(test_features.get_num_vectors())
	print "data dimension = " + str(test_features.get_num_features())

	return train_features, train_labels, test_features, test_labels

def knn(train_features, train_labels, test_features, test_labels, k=1):
	from modshogun import KNN, MulticlassAccuracy, EuclideanDistance

	distance = EuclideanDistance(train_features, train_features)
	knn = KNN(k, distance, train_labels)
	knn.train()
	train_output = knn.apply()
	test_output = knn.apply(test_features)
	evaluator = MulticlassAccuracy()
	print 'KNN training error is %.4f' % ((1-evaluator.evaluate(train_output, train_labels))*100)
	print 'KNN test error is %.4f' % ((1-evaluator.evaluate(test_output, test_labels))*100)

def lmnn(train_features, train_labels, test_features, test_labels, k=1):
	from modshogun import LMNN, KNN, MSG_DEBUG, MulticlassAccuracy
	import numpy

# 	dummy = LMNN()
# 	dummy.io.set_loglevel(MSG_DEBUG)

	lmnn = LMNN(train_features, train_labels, k)
	lmnn.train()
	distance = lmnn.get_distance()

	knn = KNN(k, distance, train_labels) 
	knn.train()

	train_output = knn.apply()
	test_output = knn.apply(test_features)
	evaluator = MulticlassAccuracy()
	print 'LMNN training error is %.4f' % ((1-evaluator.evaluate(train_output, train_labels))*100)
	print 'LMNN test error is %.4f' % ((1-evaluator.evaluate(test_output, test_labels))*100)

# 	# remove mean from the features 
# 	from modshogun import PruneVarSubMean
# 	submean = PruneVarSubMean(False)
# 	train_mat = m_data_dict['xTr'][:,:n].astype(numpy.float64)
# 	train_features_pca = RealFeatures(train_mat)
# 	submean.init(train_features_pca)
# 	submean.apply_to_feature_matrix(train_features_pca)

def lmnn_diagonal(train_features, train_labels, test_features, test_labels, k=1):
	from modshogun import LMNN, KNN, MSG_DEBUG, MulticlassAccuracy
	import numpy

	lmnn = LMNN(train_features, train_labels, k)
	lmnn.set_diagonal(True)
	lmnn.train()
	distance = lmnn.get_distance()

	knn = KNN(k, distance, train_labels) 
	knn.train()

	train_output = knn.apply()
	test_output = knn.apply(test_features)
	evaluator = MulticlassAccuracy()
	print 'LMNN-diagonal training error is %.4f' % ((1-evaluator.evaluate(train_output, train_labels))*100)
	print 'LMNN-diagonal test error is %.4f' % ((1-evaluator.evaluate(test_output, test_labels))*100)

def mkl(train_features, train_labels, test_features, test_labels, width=5, C=1.2, epsilon=1e-2, mkl_epsilon=0.001, mkl_norm=2):
	from modshogun import CombinedKernel, CombinedFeatures
	from modshogun import GaussianKernel, LinearKernel, PolyKernel
	from modshogun import MKLMulticlass, MulticlassAccuracy

	kernel = CombinedKernel()
	feats_train = CombinedFeatures()
	feats_test = CombinedFeatures()

	feats_train.append_feature_obj(train_features)
	feats_test.append_feature_obj(test_features)
	subkernel = GaussianKernel(10,width)
	kernel.append_kernel(subkernel)

	feats_train.append_feature_obj(train_features)
	feats_test.append_feature_obj(test_features)
	subkernel = LinearKernel()
	kernel.append_kernel(subkernel)

	feats_train.append_feature_obj(train_features)
	feats_test.append_feature_obj(test_features)
	subkernel = PolyKernel(10,2)
	kernel.append_kernel(subkernel)

	kernel.init(feats_train, feats_train)
	mkl = MKLMulticlass(C, kernel, train_labels)

	mkl.set_epsilon(epsilon);
	mkl.set_mkl_epsilon(mkl_epsilon)
	mkl.set_mkl_norm(mkl_norm)

	mkl.train()
	train_output = mkl.apply()

	kernel.init(feats_train, feats_test)

	test_output = mkl.apply()
	evaluator = MulticlassAccuracy()
	print 'MKL training error is %.4f' % ((1-evaluator.evaluate(train_output, train_labels))*100)
	print 'MKL test error is %.4f' % ((1-evaluator.evaluate(test_output, test_labels))*100)

def lda(train_features, train_labels, test_featues, test_labels):
	from modshogun import MCLDA, MulticlassAccuracy

	lda = MCLDA(train_features, train_labels)
	lda.train()

	train_output = lda.apply()
	test_output = lda.apply(test_features)
	evaluator = MulticlassAccuracy()
	print 'LDA training error is %.4f' % ((1-evaluator.evaluate(train_output, train_labels))*100)
	print 'LDA test error is %.4f' % ((1-evaluator.evaluate(test_output, test_labels))*100)

def qda(train_features, train_labels, test_featues, test_labels):
	from modshogun import QDA, MulticlassAccuracy

	qda = QDA(train_features, train_labels)
	qda.train()

	train_output = qda.apply()
	test_output = qda.apply(test_features)
	evaluator = MulticlassAccuracy()
	print 'QDA training error is %.4f' % ((1-evaluator.evaluate(train_output, train_labels))*100)
	print 'QDA test error is %.4f' % ((1-evaluator.evaluate(test_output, test_labels))*100)

def shareboost(train_features, train_labels, test_features, test_labels):
	from modshogun import ShareBoost, MulticlassAccuracy, RealSubsetFeatures

	shareboost = ShareBoost(train_features, train_labels, min(train_features.get_num_features()-1, 30))
	shareboost.train()

	feats_test = RealSubsetFeatures(test_features, shareboost.get_activeset())
	test_output = shareboost.apply(feats_test)
	evaluator = MulticlassAccuracy()
	print 'ShareBoost test error is %.4f' % ((1-evaluator.evaluate(test_output, test_labels))*100)


if __name__ == '__main__':
	train_features, train_labels, test_features, test_labels = load_data(num_train_samples=2000)
	shareboost(train_features, train_labels, test_features, test_labels)
	qda(train_features, train_labels, test_features, test_labels)
	lda(train_features, train_labels, test_features, test_labels)
	knn(train_features, train_labels, test_features, test_labels, 5)
	mkl(train_features, train_labels, test_features, test_labels)
	lmnn(train_features, train_labels, test_features, test_labels, 5)
	lmnn_diagonal(train_features, train_labels, test_features, test_labels, 5)
