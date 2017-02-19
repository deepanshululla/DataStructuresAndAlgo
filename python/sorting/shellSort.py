def shellSort(alist2):
	alist=alist2
	gapLength=len(alist)//2
	while gapLength>0:
		for startPosition in range(gapLength):
				gapInsertionSort(alist,startPosition,gapLength)
		
		print("After increments of size",gapLength,"The list is",alist)
		gapLength=gapLength//2
	return alist
		
		
def gapInsertionSort(list1,startPosition,gapLength):
	gap=gapLength
	alist=list1
	for i in range(startPosition+gap,len(alist),gapLength):
		currentValue=alist[i]# currentValue is taken as a tem variable
		position=i
		while position>=gap and alist[position-gap]>currentValue:
			alist[position]=alist[position-gap]
			position=position-gap
	
		alist[position]=currentValue
	
		
alist = [5, 16, 20, 12, 3, 8, 9, 17, 19, 7] 
print("the original list",alist)
shellSort(alist)
print(alist)