


# Create the Node or Neuron
#	- this Node can only be connected
#	to a maximum of 3 Nodes
#------------------------

class Node(object):

	def __init__(self, data, n1, n2, n3):
		self.data = data
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
		
	def setN(self, n):
		if n==0:
			self.n1 = n
		elif n==1:
			self.n2 = n
		elif n==3:
			self.n3 = n

#------------------------



# Create the Linked List of Nodes
#	- this is the set of interconnected nodes
#	 that will be used in ann structure
#------------------------

class NodeList(object):

	def __init__(self, head):
		self.head = head

	def insert(self, data):
		new_node = Node(data)
		new_node.setNext(self.head)
		self.head = new_node

	def size(self):
		current = self.head
		length = 0
		while current:
			length+=1
			current = current.getNext()
		return length

	def search(self, data):
		current = self.head
		found = False
		while current and not found:
			if current.getData() == data:
				found = True
			else:
				current = current.getNext()
		if current is None:
			print("Data not in list")
		return current

	def delete(self, data):
		current = self.head
		previous = None
		found = False
		while current and not found:
			if current.getData() == data:
				found = True
			else:
				previous = current
				current = current.getNext()
		if current is None:
			print("Data not in list")
		if previous is None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())

#------------------------


