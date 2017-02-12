#!/usr/bin/python



		
def mergeSort(array):
		#self.a=array
	print("Splitting ",array)
	length=len(array)
	
	if length>1:	
		mid=length//2
		leftHalf=array[:mid]
		rightHalf=array[mid:]
		#print("Lefthalf ",leftHalf)
		mergeSort(leftHalf)
		#print("Righthalf ",rightHalf)
		
		mergeSort(rightHalf)
		

		l1=len(leftHalf)
		l2=len(rightHalf)
		

		
		i=0
		j=0
		k=0
		while i<l1 and j<l2:
			if leftHalf[i]<rightHalf[j]:
				#print i,j,k
				array[k]=leftHalf[i]
				i=i+1
				
			else:
				#print i,j,k
				array[k]=rightHalf[j]
				j=j+1
			
			k=k+1
			
		while i<l1:
			#print i,j,k
			array[k]=leftHalf[i]
			i=i+1
			k=k+1
			
		while j<l2:
			array[k]=rightHalf[j]
			j=j+1
			k=k+1
			
		print(array)	
		
			
array=[2,4,5,5,2,0,1,5,7,7,9]				


mergeSort(array)
print array