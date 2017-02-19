def selectionSort(list1):
	alist=list1
	for fillSlot in range(len(alist)-1,0,-1):	
		posOfMax=0
		for location in range(1,fillSlot+1):
			if alist[location]>alist[posOfMax]:
				posOfMax=location
		
		temp=alist[fillSlot]
		alist[fillSlot]=alist[posOfMax]
		alist[posOfMax]=temp
		
	return alist
list1 = [54,26,93,17,77,31,44,55,20]
alist=selectionSort(list1)
print(alist)
