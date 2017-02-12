#written by myself 

#pivot is the last element in array. then we didvide array into two halfs less than equal to pivot.
#inplace but not stable
def quickSortHelper(A,start,end):
	if start<end:
		split=partition(A,start,end)
		print("starting rec1")
		quickSortHelper(A,start,split-1)
		print("starting rec2")
		quickSortHelper(A,split+1,end)


def partition(A,start,end):
	print(A)
	i=start-1
	val=A[end]
	print("Pivot element is %d"%(val))
	for j in range(start,end):
		if A[j]<val:
			i=i+1
			if A[i]!=A[j]:
				A[i],A[j]=A[j],A[i]
				print("Swapping %d and %d"%(A[i],A[j]))
	if A[i+1]!=A[end]:		
		A[i+1],A[end]=A[end],A[i+1]
		print("Swapping %d and %d"%(A[i+1],A[end]))
	split=i+1
	print("Splitpoint=%d"%split)
	return split
	

def quickSort(array1):
	#print(array1)
	quickSortHelper(array1,0,len(array1)-1)
	print(array1)
array=[12,9,6,2,5,8,1,3,5,41]
#array=[1,1,1,1]
quickSort(array)