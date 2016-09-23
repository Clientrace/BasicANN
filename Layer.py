import random


class Layer(object):
	def __init__(self, name, node_number):
		self.nodes = []
		self.name = name
		self.data = 0
		self.weights = []
		for i in range(0,node_number):
			self.nodes.append(0)
			self.weights.append(random.random())

	def getData(self, n):
		return self.nodes[n]

	def setData(self, data, n):
		self.nodes[n] = data

	def setWeight(self, w):
		self.weight = weight

	def getWeight(self):
		return self.weight