import matplotlib.pyplot as pyplot
import numpy
import pickle
from scipy import io

data_dict = io.loadmat('/home/iglesias/workspace/lmnn/mLMNN2.4/original_lmnn_diagonal_ape_gut.mat')
mlmnn_linear_transform = data_dict['Lk']
mlmnn_diagonal = numpy.diag(mlmnn_linear_transform)

shogun_lmnn = pickle.load(open('lmnn_ape_gut_trained.p', 'rb'))
shogun_linear_transform = shogun_lmnn.get_linear_transform()
shogun_diagonal = numpy.diag(shogun_linear_transform)

pyplot.scatter(shogun_diagonal, mlmnn_diagonal)
pyplot.title('Shogun vs. mLMNN2.4 diagonal transform in ape gut data set')
pyplot.xlabel('Shogun diagonal')
pyplot.ylabel('mLMNN diagonal')
pyplot.grid(True)
pyplot.show()
