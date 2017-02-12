#!/usr/bin/python

#this is stablein place version of insertionSort  
def insertionSort(A):
	for index in range(1,len(A)):
		val=A[index]
		position=index
		
		while position>0 and val<A[position-1]:
			A[position]=A[position-1]
			position=position-1
			print "Sorted", array	
		A[position]=val
		print A

			
array=[2,5,4,5,2,0,1,5,7,7,9]				


insertionSort(array)
print "Sorted", array		
	


