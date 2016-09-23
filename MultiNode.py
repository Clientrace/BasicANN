

# Create the Node or Neuron
#	- this Node can only be connected
#	to a maximum of 3 Nodes
#------------------------

class Node(object):

	def __init__(self, data, n1, n2, n3):
		self.data = data
		self.weight = 0
		self.n1 = n1
		self.n2 = n2
		self.n3 = n3

	def getData(self):
		return self.data

	def getN(self, n):
		if n==0:
			return self.n1
		elif n==1:
			return self.n2
		elif n==2:
			return self.n3
		return None
		
	def setN(self, N, n):
		if n==0:
			self.n1 = N
		elif n==1:
			self.n2 = N
		elif n==3:
			self.n3 = N

	def setWeight(self,weight):
		self.weight = weight

#------------------------



# Create the Linked List of Nodes
#	- this is the set of interconnected nodes
#	 that will be used in ann structure
#------------------------

class NodeList(object):

	def __init__(self, head):
		self.head = head
		self.parent = head

	def insert(self, data, n):
		if n>3:
			return None
		if n==0:
			new_node = Node(data,n,0,0)
		elif n==1:
			new_node = Node(data,0,n,0)
		elif n==2:
			new_node = NodeList(data,0,0,n)
		new_node.setN(self.head,n)
		self.head = new_node

	def getHead(self):
		return self.head

	def showData(self):
		print(self.head.getData())

	def next(self, n):
		self.head = self.head.getN(n)

	def parent(self, n):
		self.head = self.parent

#------------------------


