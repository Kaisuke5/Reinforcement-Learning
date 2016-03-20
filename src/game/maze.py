import numpy as np
import problem
import matplotlib.pyplot as plt

class maze(problem.problem):

	def __init__(self,width,height,action,goal,default_q=0.5,default_reward=0,goal_reward=1,iter=20,fname='output.jpg',epoch=2000):
		self.width =width
		self.height = height
		self.act = np.array(action)
		self.default_reward = default_reward
		self.goal_reward = goal_reward
		self.default_q = default_q
		# self.field = np.array()
		self.goal = np.array(goal)
		self.reward = {}
		self.iter = iter
		self.count = 0
		self.all_count = 0
		self.path = []
		self.map = np.zeros([width,height])




	def init_problem(self):
		state_list = [np.array([x,y]) for x in range(self.width) for y in range(self.height)]
		q = {}

		for id in state_list:
			q[str(id)] = np.random.random(len(self.act)) * 0.1 + 0.5
			self.reward[str(id)] = self.default_reward

		self.set_reward()
		self.show_map(q,"init.jpg")
		return q,np.array([0,0])

	def set_reward(self):
		self.reward[str(self.goal)] = self.goal_reward


	def action(self,s,a):
		self.count += 1
		self.all_count += 1

		new_s = s + self.act[a]
		#print new_s,self.goal,(new_s == self.goal).all()

		if self.count > self.iter:
			print 'no goal last%s' % (self.path[-2:])
			self.path = [[0,0]]
			self.count = 0
			return 'reset',np.array([0,0]), None

		elif (new_s == self.goal).all():
			print 'goal and reset..%d walked!!' % len(self.path)
			self.path = [[0,0]]
			self.count = 0

			return 'goal',self.goal, self.reward[str(new_s)]

		else:

			if np.min(new_s) < 0 or new_s[0] >= self.width or new_s[1] >= self.height:
				self.count -= 1
				return "invalid road",None,None
			self.path.append(new_s)
			return 'action',new_s, self.reward[str(new_s)]


	def show_map(self,q,fname):

		for k,v in q.items():
			x,y = map(int,str(np.array(k))[1:-1].split())
			self.map[x][y] = np.mean(v)

		plt.imshow(self.map, interpolation='none')
		plt.savefig(fname)


	def random_start(self):
		return np.array([np.random.randint(0,self.width),np.random.randint(0,self.height)])



if __name__ == "__main__":
	m = maze(5, 5, [[1,0], [0,1]], [4,4])
	q,r = m.init_problem()
	m.show_map(q)


