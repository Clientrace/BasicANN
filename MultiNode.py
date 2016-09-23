

# Create the Node or Neuron
#	- this Node can only be connected
#	to a maximum of 3 Nodes
#------------------------

class Node(object):

	def __init__(self, data):
		self.data = data
		self.weight = 0
		self.head1 = None
		self.head2 = None
		self.head3 = None

	def setWeight(self, weight):
		self.weight = weight

	def getWeigth(self, weight):
		return self.weight

	def setData(self, data):
		self.data = data

	def getData(self):
		return self.data

	def next(self, n):
		if n==0:
			return self.head1
		elif n==1:
			self.head = self.head2
			return self.head2
		elif n==2:
			self.head = self.n3
			return self.head3
		return None

	def connect(self, N, N2, N3):
		self.head1 = N
		self.head2 = N2
		self.head3 = N3

#------------------------

