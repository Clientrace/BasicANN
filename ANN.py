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
# 0 0		1
# 0 1		0
# 1 0		0
# 1 1		1
#
#------------------------

def main():

	#Input Layers
	#---------------------

	Input1 = Node(3)
	Input2 = Node(0)
	
	#---------------------

	#Hidden Layers
	#---------------------
	
	Hidden1 = Node(2)
	Hidden2 = Node(0)
	
	Hidden3 = Node(0)
	#---------------------

	#Output Layer
	#---------------------
	
	Output = Node(1)
	
	#---------------------

	#Connect the layers
	#---------------------
	
	Input1.connect(Hidden1,Hidden2,Hidden3)
	
	Hidden1.connect(Input1,Input2,None)
	Hidden2.connect(Input1,Input2,None)
	Hidden3.connect(Input1,Input2,None)

	
	Output.connect(Hidden1,Hidden2,Hidden3)
	#---------------------

	
	
main()