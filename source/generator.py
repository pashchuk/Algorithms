from random import randint

def Generate(len,maxValue):
	a=[]
	for i in range(len):
		a.append(randint(0,maxValue))
	return a