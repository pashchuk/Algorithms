import generator

def BubleSort(array):
	for i in xrange(len(array)):
		for j in xrange(len(array)-i-1):
			if array[j]>array[j+1]:
				array[j], array[j+1] = array[j+1], array[j]


def main():
	a=generator.Generate(30,100)
	print a
	BubleSort(a)
	print a

if __name__ == "__main__":main()