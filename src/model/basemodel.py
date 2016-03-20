class baseagent:

	def __init__(self,problem):
		self.problem = problem
		self.q_value, self.s = problem.init_problem()
		self.a = None
		self.p_s = None
		self.r = None

	def select_action(self):
		raise NotImplementedError



	def take_action(self,a):
		raise NotImplementedError




	#update q_value
	def update(self):
		raise NotImplementedError


	def learn(self):
		raise NotImplementedError


	def solve(self):
		raise NotImplementedError