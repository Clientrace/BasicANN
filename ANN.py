import random
import math
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
global learned


#Get XOR Value For The Training
#------------------------
def getXOR(input1, input2):
	if(input1==input2):
		return 0
	return 1

#Sigmoid Function
#This is the acitivation function to transform
#the input signal to output signal.
#Formula: S(t) = 1/1+e^-t
#------------------------
def sigmoid(t):
	return (1/(1+math.exp(-t)))

#Initialize The Nodes
#------------------------
def init():
	global trainingFile
	global inputLayer
	global hiddenLayer
	global outputLayer

	inputLayer = Layer("InputLayer",2)
	hiddenLayer = Layer("HiddenLayer",3)
	outputLayer = Layer("OutputLayer",3)
	
	
#------------------------

def testANN(input1, input2):
	print("testing...")
	global trainingFile
	global inputLayer
	global hiddenLayer
	global outputLayer

	print("training...")

	idealOutput = getXOR(input1,input2)

	inputLayer.setData(input1,0)
	inputLayer.setData(input2,1)

	outputLayer.setData(idealOutput,0)

	#Calculate hidden layer values
	for i in range(0,3):
		hiddenVal1 = (float(inputLayer.getData(0))*float(hiddenLayer.getWeight(i)))
		hiddenVal2 = (float(inputLayer.getData(1))*float(hiddenLayer.getWeight(i)))
		nodeVal = sigmoid((hiddenVal1+hiddenVal2))
		hiddenLayer.setData(nodeVal,i)

	#Calculate the output value
	outputVal = 0
	for i in range(0,3):
		outputLayer.getWeight(i)*hiddenLayer.getData(i)
		outputVal+=outputLayer.getWeight(i)*hiddenLayer.getData(i)
	outputLayer.setData(outputVal,0)


def train(input1, input2):
	global trainingFile
	global inputLayer
	global hiddenLayer
	global outputLayer

	print("training...")

	idealOutput = getXOR(input1,input2)

	inputLayer.setData(input1,0)
	inputLayer.setData(input2,1)

	outputLayer.setData(idealOutput,0)

	#Calculate hidden layer values
	for i in range(0,3):
		hiddenVal1 = (float(inputLayer.getData(0))*float(hiddenLayer.getWeight(i)))
		hiddenVal2 = (float(inputLayer.getData(1))*float(hiddenLayer.getWeight(i)))
		nodeVal = sigmoid((hiddenVal1+hiddenVal2))
		hiddenLayer.setData(nodeVal,i)

	#Calculate the output value
	outputVal = 0
	for i in range(0,3):
		outputLayer.getWeight(i)*hiddenLayer.getData(i)
		outputVal+=outputLayer.getWeight(i)*hiddenLayer.getData(i)
	outputLayer.setData(outputVal,0)
	


#Shows the neural network structure
#------------------------

def showStruct():
	global inputLayer
	global hiddenLayer
	global outputLayer
	if learned:
		print("+-------+-----------------------+------------------------+")
		print("| INPUT | HIDDEN \t\t| OUTPUT\t\t |")
		print("+-------+-----------------------+------------------------+")
		print("| "+str(inputLayer.getData(0))+"\t| "+str(hiddenLayer.getData(0))+"\t| "+str(outputLayer.getData(0))+"\t |")
		print("| "+str(inputLayer.getData(1))+"\t| "+str(hiddenLayer.getData(1))+"\t| \t\t\t |")
		print("| \t| "+str(hiddenLayer.getData(2))+"\t| \t\t\t |")
		print("+-------+-----------------------+------------------------+")
	else:
		print("+-------+-----------------------+------------------------+")
		print("| INPUT | HIDDEN                | OUTPUT 				|")
		print("+-------+-----------------------+------------------------+")
		print("| 0     | 0					   | 0						|")
		print("| 0     | 0					   |						|")
		print("|       | 0					   |						|")
		print("+-------+-----------------------+------------------------+")
#------------------------

#------------------------


#main function
#------------------------
def main():
	init()
	print("Simple ANN (c) 2016")
	print("-----------------------")
	while True:
		print(">> ",end='')
		command = input()
		print(command)
		if(command == "test"):
			print("Enter input1: ")
			i = input()
			print("Enter input2: ")
			i2 = input()
			train(i,i2)
			showStruct()
			learned = True
		if(command == "showstruct"):
			showStruct()
	
#------------------------

	

main()