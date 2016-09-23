import random
from Layer import Layer


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

global trainingFile
global inputLayer
global hiddeLayer
global outputLayer


#Get XOR Value For The Training
#------------------------
def getXOR(input1, input2):
	if(input1==input2):
		return 0
	return 1

#Initialize The Nodes
#------------------------
def init():
	global trainingFile
	global inputLayer
	global hiddenLayer
	global outputLayer

	inputLayer = Layer("InputLayer",2)
	hiddenLayer = Layer("HiddenLayer",3)
	outputLayer = Layer("OutputLayer",1)
	
	
#------------------------

def testANN(input1, input2):
	print("testing...")

def train(input1, input2):
	global trainingFile
	global inputLayer
	global hiddenLayer
	global outputLayer

	print("training...")

	idealOutput = getXOR(input1,input2)

	inputLayer.setData(input1,0)
	inputLayer.setData(input2,1)
	
	outputLayer.setData(idealOutput)

	for i in range(0,3):
		hiddenLayer.setData(0,0)

	


#Shows the neural network structure
#------------------------

def showStruct():
	print("+-------+--------+-------+")
	print("| INPUT | HIDDEN | OUTPUT")
	print("+-------+--------+-------+")
#------------------------

#------------------------


#main function
#------------------------
def main():
	init()
	print("I: ")
	i = input()
	print("I2: ")
	i2 = input()
	train(i,i2)
	
#------------------------

	

main()