import numpy as np

class problem:

	#return q_value and initial state
	def init_problem(self):
		raise NotImplementedError


	def action(self,s,a):
		raise NotImplementedError


	def set_reward(self):
		raise NotImplementedError



	def id(self,s,t):
		return str(s) + str("%") + str(t)


