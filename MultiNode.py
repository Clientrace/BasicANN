import random

# Create the Node or Neuron
#	- this Node can only be connected
#	to a maximum of 3 Nodes
#------------------------

class Node(object):

	def __init__(self, data):
		self.data = data
		self.next = next


	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setNext(self,next):
		self.next = next



#------------------------

class NodeList():

	def __init__(self, name, head1, head2, head3):
		self.curHead = None
		self.prev = None
		self.head1 = head1
		self.head2 = head2
		self.head3 = head3

		self.weight1 = random.random()
		self.weight2 = random.random()
		self.weight3 = random.random()

		self.name = name

	def getData(self):
		return self.curHead.getData()

	def getWeight(self, n):
		if n==0:
			return self.weight1
		if n==1:
			return self.weight2
		if(n==2):
			return self.weight3

	def setWeight(self, weight, n):
		if n==0:
			return self.weight1
		if n==1:
			return self.weight2
		if(n==2):
			return self.weight3


	def addNode(self, data, name, n):
		if n==0:
			new_node = Node(data)
			new_node.setNext(self.head1)
		if n==1:
			new_node = Node(data)
			new_node.setNext(self.head2)
			curHead = new_node
		if(n==2):
			new_node = Node(data)
			new_node.setNext(self.head3)

	def next(self, n):
		if n==0:
			prev = curHead
			curHead = head1
		if n==1:
			prev = curHead
			curHead = head2
		if n==2:
			prev = curHead
			curHead = head3

	def prev(self, n):
		curHead = prev



