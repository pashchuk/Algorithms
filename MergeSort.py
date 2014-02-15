import generator

def MergeSort(array):
	if len(array) <= 1:
		return array
	else:
		left = []
		right = []
		mid = len(array)/2
		for x in xrange(0,mid):
			left.append(array[x])
		for x in xrange(mid,len(array)):
			right.append(array[x])
		left = MergeSort(left)
		right = MergeSort(right)
		rez = Merge(left,right)
		return rez

def Merge(left,right):
	rez = []
	while len(left)>0 and len(right)>0:
		if left[0] <= right[0]:
			rez.append(left.pop(0))
		else:
			rez.append(right.pop(0))
	if len(left)>0:
		for x in left:
			rez.append(x)
	if len(right)>0:
		for x in right:
			rez.append(x)
	return rez



def main():
	a = generator.Generate(10,100)
	print a
	a = MergeSort(a)
	print a

if __name__ == "__main__":main()