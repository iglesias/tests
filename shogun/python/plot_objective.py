#!/usr/bin/python

import matplotlib.pyplot as pyplot
import pickle
import sys
import numpy

# Default number of objective values to plot, starting from the last iteration.
DEFAULT_NUMEL = 50

if len(sys.argv) < 2:
  numel = DEFAULT_NUMEL
else:
  try:
    numel = int(sys.argv[1])
  except ValueError:
    numel = DEFAULT_NUMEL

lmnn = pickle.load(open('backup/lmnn_ape_gut_trained.p', 'rb'))
statistics = lmnn.get_statistics()
obj = statistics.obj.get()
obj1 = obj[:20]
print numpy.abs(numpy.diff(obj1))
obj2 = obj[-20:]
print numpy.abs(numpy.diff(obj2))
pyplot.plot(obj)
pyplot.grid(True)
pyplot.xlabel('Number of iterations')
pyplot.ylabel('LMNN-diagonal objective')
pyplot.show()
