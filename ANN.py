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
#------------------------

#Derrivative of Sigmoid
#This for the computation of MOE slope for 
#weight adjustments.
#Formula: d/dx S(x) = (e^-x)/(1+e^-x)^2
#------------------------
def sigmoidPrime(t):
	return (math.exp(-t))/(math.pow((1+math.exp(-t)),2))
#------------------------

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
	global trainingFile
	global inputLayer
	global hiddenLayer
	global outputLayer

	idealOutput = getXOR(input1,input2)
	print("Expected Output: "+str(idealOutput))

	inputLayer.setData(input1,0)
	inputLayer.setData(input2,1)

	outputLayer.setData(0,0)


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

	MOE = outputLayer.getData(0) - idealOutput


def trainANN(input1, input2):
	global trainingFile
	global inputLayer
	global hiddenLayer
	global outputLayer

	idealOutput = getXOR(input1,input2)
	print("Expected Output: "+str(idealOutput))

	inputLayer.setData(input1,0)
	inputLayer.setData(input2,1)

	outputLayer.setData(0,0)

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

	#Calculate the margin of Error
	MOE = idealOutput - outputLayer.getData(0)
	showStruct()
	print("Margin Of Error: "+str(MOE))

def showWeights():
	global trainingFile
	global inputLayer
	global hiddenLayer
	global outputLayer

	print("Input -> HiddenLayer:")
	for i in range(0,3):
		print("w["+str(i)+"]:"+str(hiddenLayer.getData(i)))
	
	print("HiddenLayer -> OutputLayer:")
	for i in range(0,3):
		print("w["+str(i)+"]:"+str(outputLayer.getData(i)))


#Shows the neural network structure
#------------------------

def showStruct():
	global inputLayer
	global hiddenLayer
	global outputLayer
	global learned
	if learned:
		print("+-------+-----------------------+------------------------+")
		print("| INPUT | HIDDEN \t\t| OUTPUT\t\t |")
		print("+-------+-----------------------+------------------------+")
		print("| "+str(inputLayer.getData(0))+"\t| "+str(hiddenLayer.getData(0))+"\t| "+str(outputLayer.getData(0))+"\t |")
		print("| "+str(inputLayer.getData(1))+"\t| "+str(hiddenLayer.getData(1))+"\t| \t\t\t |")
		print("| \t| "+str(hiddenLayer.getData(2))+"\t| \t\t\t |")
		print("+-------+-----------------------+------------------------+")
	else:
		print("+-------+-----------------------+-----------------------+")
		print("| INPUT | HIDDEN                | OUTPUT  \t\t|")
		print("+-------+-----------------------+-----------------------+")
		print("| 0     | 0	\t\t| 0	\t\t|")
		print("| 0     | 0	\t\t|	\t\t|")
		print("|       | 0	\t\t|	\t\t|")
		print("+-------+-----------------------+-----------------------+")
#------------------------

#------------------------


#main function
#------------------------
def main():
	global learned
	learned = False
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
			testANN(i,i2)
			learned = True
			showStruct()
		if(command == "train"):
			print("Enter input1: ")
			i = input()
			print("Enter input2: ")
			i2 = input()
			learned = True
			trainANN(i, i2)
		if(command == "showstruct"):
			showStruct()
		if(command == "weights"):
			showWeights()
	
#------------------------

	

main()