import random
from MultiNode import Node


"""
	Author: Kim Clarence Penaflor
	Email:  pkimclarence@yahoo.com.ph |
			clientrace4869@gmail.com
"""

#------------------------
#
# XOR Machine Learning
#
# INPUT | IDEAL
# 0 0		0
# 0 1		1
# 1 0		1
# 1 1		0
#
#------------------------

global Input1
global Input2
global Hidden1
global Hidden2
global Hidden3
global Output
global trainingFile

#get xor value for the training
#------------------------
def getXOR(input1, input2):
	if(input1==input2):
		return 0
	return 1


#initialize the nodes
#------------------------
def init():

	global trainingFile
	global Input1
	global Input2
	global Hidden1
	global Hidden2
	global Hidden3
	global Output

	#load training file
	trainingFile = open('TrainingFiles/tf.ann','a')

	#Input Layers
	Input1 = Node(3)
	Input2 = Node(0)

	#Hidden Layers
	Hidden1 = Node(2)
	Hidden2 = Node(0)
	
	Hidden3 = Node(0)

	#Output Layer
	Output = Node(1)

	#Connect the layers
	Input1.connect(Hidden1,Hidden2,Hidden3)
	Hidden1.connect(Input1,Input2,None)
	Hidden2.connect(Input1,Input2,None)
	Hidden3.connect(Input1,Input2,None)
	Output.connect(Hidden1,Hidden2,Hidden3)
#------------------------

def testANN(input1, input2):
	print("testing...")

def train():
	print("training..")


def main():
	init()
	

main()