
import generator

def InsertionSort(array):
	for i in xrange(1,len(array)):
		temp=array[i]
		j=i-1
		while temp < array[j] and j >= 0:
			array[j+1] = array[j]
			j-=1
		array[j+1] = temp


def main():
	a=generator.Generate(10,100)
	print a
	InsertionSort(a)
	print a

if __name__ == "__main__":main()