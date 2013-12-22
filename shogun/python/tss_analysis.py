#!/usr/bin/python

import numpy
import utils
from modshogun import *


def generate_sequence_limits(num_elem=690411):
  '''
  Generate indices to split the long sequence in shorter ones.
  The length of the new subsequences is drawn from an integer Uniform(a,b) distribution with both
  ends included.
      a has been fixed to 1000 as a lower bound for the sequence length.
      b has been chosen so that the average sequence length gives rise to about 50 sequences.
  '''
  seq_limits = list()
  seq_lens = list()

  a = 1000
  b = 26616

  while True:
    rand_len = numpy.random.randint(a, b+1) # +1 because numpy's randint draws from [a,b)
    seq_lens.append(rand_len)

    if len(seq_limits) == 0:
      seq_limits.append([0, rand_len-1])
    else:
      num_elem_left = num_elem - (seq_limits[-1][1]+1)
      if num_elem_left < a:
        print 'The last sequence is shorter than the lower bound of the uniform distribution'
        seq_limits.append([seq_limits[-1][1]+1, num_elem-1])
        seq_lens[-1] = seq_limits[-1][1] - seq_limits[-1][0] + 1
        break
      elif num_elem_left <= b:
        seq_limits.append([seq_limits[-1][1]+1, num_elem-1])
        seq_lens[-1] = seq_limits[-1][1] - seq_limits[-1][0] + 1
        break
      else:
        seq_limits.append([seq_limits[-1][1]+1, seq_limits[-1][1]+rand_len])

  print '%d sequences with average length equal to %f' % (len(seq_lens), numpy.mean(seq_lens))
  return seq_limits

print 'Loading data...'
TSS_example = numpy.loadtxt('../data/TSS_example.txt')
# TSS_example = numpy.loadtxt('../data/TSS_example_small.txt')
print '\tdone!'

state_seq = TSS_example[:,1].astype(numpy.int32) # all the states concatenated in a very long sequence
feat_mat = TSS_example[:,2:].T
assert(state_seq.shape[0] == feat_mat.shape[1])
num_elem = state_seq.shape[0]
num_features = feat_mat.shape[0]

seq_limits = generate_sequence_limits(num_elem)
labels = SequenceLabels(len(seq_limits), 2)
features = RealMatrixFeatures(len(seq_limits), num_features)

for i in xrange(len(seq_limits)):
  lo, hi = seq_limits[i]
  labels.add_vector_label(state_seq[lo:hi+1])
  features.set_feature_vector(feat_mat[:, lo:hi+1], i)

print 'num_labels=%d' % labels.get_num_labels()
print 'num_states=%d' % labels.get_num_states()
print 'num_features=%d' % features.get_num_features()
print 'num_vectors=%d' % features.get_num_vectors()

model = HMSVMModel(features, labels, SMT_TWO_STATE)
model.set_use_plifs(True)
# sosvm = DualLibQPBMSOSVM(model, labels, 5000.0)
# sosvm = StochasticSOSVM(model, labels)
# sosvm.set_lambda(1)
# sosvm.set_verbose(True)
hinge_loss = HingeLoss()
sosvm = PrimalMosekSOSVM(model, labels)
sosvm.set_regularization(50)
sosvm.io.set_loglevel(MSG_DEBUG)

print 'Training SO-SVM...'
sosvm.train()
print '\tdone!'
print sosvm.get_w()

predicted = sosvm.apply(model.get_features())
evaluator = StructuredAccuracy()
acc = evaluator.evaluate(predicted, model.get_labels())
print 'Training accuracy = %.4f' % acc
utils.print_statistics(labels, predicted)
