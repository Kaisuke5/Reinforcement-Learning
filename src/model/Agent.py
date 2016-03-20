import numpy as np
from basemodel import baseagent
import sys

sys.path.append("/Users/kaishunsuke/work/machine-learning/Reinforcement-learning/src/")
from game.maze import maze

class agent(baseagent):

	def __init__(self,problem,gamma=0.9,iter=1000,e=0.1,alpha=0.3):
		baseagent.__init__(self,problem)
		self.type = type
		self.i = iter
		self.e = e
		self.gamma = gamma
		self.alpha = alpha
		self.epoch = 0



	def select_action(self):

		if np.random.random(1) > self.e:
			return self.q_value[str(self.s)].argmax()
		else:
			return np.random.randint(0,len(self.q_value[str(self.s)]))


	def update(self):
		t = str(self.p_s)
		tp = str(self.s)
		a = self.a
		tmp = self.q_value[t][a]
		diff = np.max(self.q_value[tp]) - tmp
		self.q_value[t][a] += self.alpha * (self.r + self.gamma * diff)
		# if diff > 0.1:
			# print self.s,self.p_s,self.alpha * (self.r + self.gamma * np.max(diff))



	def take_action(self,a):
		message, new_s, r = self.problem.action(self.s, a)
		if message == 'action':
			self.p_s = self.s
			self.s = new_s
			self.a = a
			self.r = r
			self.update()

		if message == "goal":
			# print "g",new_s
			self.p_s = self.s
			self.s = new_s
			self.a = a
			self.r = r
			self.update()

			self.reset()
			self.epoch += 1
			# print 'e%f' % self.e
			#print float(self.i-self.epoch)/self.i
			print 'epoch:%d alpha%f' % (self.epoch,self.alpha)
			if self.epoch % 30 == 0:
				self.problem.show_map(self.q_value,"data.jpg")
				# self.e *= (float(self.i-self.epoch)/self.i)

		if message == 'reset':
			self.reset()

		return message

	def reset(self):
		if self.epoch % 10 == 0:
			self.s = self.problem.random_start()
		else: self.s = np.array([0,0])
		self.a = None
		self.p_s = None



	def learn(self):
		while self.epoch < self.i:
			action = self.select_action()
			message = self.take_action(action)

			# if message == 'end': break




	def solve(self):
		pass


if __name__ == "__main__":
	maze = maze(30, 30, [[1,0], [0,1], [-1,0],[0,-1]], [23,18], goal_reward=1.0,iter=6000)
	print len(maze.act)

	a = agent(maze,iter=2000)
	a.learn()