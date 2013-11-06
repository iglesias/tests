#!/usr/bin/python

from modshogun import *

class CostEvaluation(ContingencyTableEvaluation):

	def init(self):
		ContingencyTableEvaluation.__init__(self, CUSTOM)
		print "Initialize evaluation"

	def set_indices(self, indices):
		print "Set indices called"
		self.custom_indices = indices
		print indices

	def evaluate(self, predicte, ground_truth):
		print "Evaluate called"
		return 0.0

	def get_custom_direction(self):
		return ED_MAXIMIZE

	def custom_score(self):
		return 1

	def get_name(self):
		return "CostEvaluation"

cost_evaluation = CostEvaluation()
print cost_evaluation.get_name()
print cost_evaluation.get_custom_direction()
