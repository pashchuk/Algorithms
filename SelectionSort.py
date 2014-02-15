import generator

def SelectionSort(array):
	for i in xrange(len(array)-1):
		minindex = i
		elem = array[minindex]
		for j in xrange(i,len(array)-1):
			if array[j] <= elem:
				elem=array[j]
				minindex=j
		array[i], array[minindex] = array[minindex], array[i]


def main():
	a=generator.Generate(30,100)
	print a
	SelectionSort(a)
	print a

if __name__ == "__main__":main()