	def __init__(self, data):
		self.data = data

		self.weight1 = random.random()
		self.weight2 = random.random()
		self.weight3 = random.random()

		self.head1 = None
		self.head2 = None
		self.head3 = None

	def setWeight(self, weight, n):
		if(n==0):
			self.weight1 = weight
		if(n==1):
			self.weight2 = weight
		if(n==2):
			self.weight3 = weight

	def getWeight(self, n):
		if(n==0):
			return self.weight1
		if(n==1):
			return self.weight2
		if(n==2):
			return self.weight3

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
			self.head = self.head3
			return self.head3
		return None

	def nextW(self, data, n):
		if n==0:
			self.head1.setData(data)
			return self.head1
		elif n==1:
			self.head2.setData(data)
			return self.head2
		elif n==2:
			self.head3.setData(data)
			return self.head3
		return None


	def connect(self, N, N2, N3):
		self.head1 = N
		self.head2 = N2
		self.head3 = N3