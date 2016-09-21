


# Create the Node or Neuron
#	- this Node can only be connected once
#------------------------

class Node(object):

	def __init__(self, data, n1, n2, n3):
		self.data = data
		self.next = next


	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setNext(self,next):
		self.next = next

#------------------------



# Create the Linked List of Nodes
#	- this is the set of interconnected linear
#	nodes that will be used in ann structure
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


