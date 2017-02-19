from timeit import default_timer
import time
def bubbleSort(list1):
	alist=list1
	for passNum in range(len(alist)-1,0,-1):
		for i in range(0,passNum):
			if alist[i]>alist[i+1]:
				temp=alist[i]
				alist[i]=alist[i+1]
				alist[i+1]=temp
		#print "after %d pass"%(len(alist)-passNum)
		#print(alist)	
	return alist;

def shortBubbleSort(list1):
	alist=list1
	exchange=True
	passNum=len(alist)-1
	while passNum>0 and exchange:
		exchange=False
		for i in range(passNum):
			if alist[i]>alist[i+1]:
				exchange=True
				temp=alist[i]
				alist[i]=alist[i+1]
				alist[i+1]=temp
		passNum=passNum-1
	return alist;

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
	

def insertionSort(list1):
	alist=list1
	for index in range(1,len(alist)):
		currentValue=alist[index]
		position=index
		while position>0 and alist[position-1]>currentValue:
			alist[position]=alist[position-1]
			position=position-1
		alist[position]=currentValue


		
def shellSort(alist2):
	alist=alist2
	gapLength=len(alist)//2
	while gapLength>0:
		for startPosition in range(gapLength):
				gapInsertionSort(alist,startPosition,gapLength)
		
		
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

def mergeSort(list1):
	alist=list1
	#print("Splitting",alist)
	if len(alist)>1:
		mid=len(alist)//2;
	
		leftHalf=alist[:mid]
		rightHalf=alist[mid:]
		mergeSort(leftHalf)
		mergeSort(rightHalf)
	
		i=0
		j=0
		k=0
		
		while i<len(leftHalf) and j<len(rightHalf):
			if leftHalf[i] <rightHalf[j]:
				alist[k]=leftHalf[i]
				i+=1
			else:
				alist[k]=rightHalf[j]
				j+=1
				
			k+=1
		while i<len(leftHalf):
			alist[k]=leftHalf[i]
			i+=1
			k+=1
		while j<len(rightHalf):
			alist[k]=rightHalf[j]
			j+=1
			k+=1
		#print("alist is ",alist)
	#print("merging list")
	return alist

		
list1 = [54,26,93,17,77,31,44,55,20]
#list1=[20,30,40,90,50,60,70,80,100,110]
	
start = default_timer()
alist=selectionSort(list1)
end_time=default_timer() - start

print "The time for selection sort is "+ str(end_time)
list1 = [54,26,93,17,77,31,44,55,20]
start = default_timer()
alist=bubbleSort(list1)
end_time=default_timer() - start

print "The time for bubble  sort is "+ str(end_time)
list1 = [54,26,93,17,77,31,44,55,20]
start = default_timer()
alist=shortBubbleSort(list1)
end_time=default_timer() - start

print "The time for short bubble sort is "+ str(end_time)
list1 = [54,26,93,17,77,31,44,55,20]

start = default_timer()
alist=insertionSort(list1)
end_time=default_timer() - start

print "The time for insertion sort is "+ str(end_time)
list1 = [54,26,93,17,77,31,44,55,20]
start = default_timer()
alist=shellSort(list1)
end_time=default_timer() - start

print "The time for shell sort is "+ str(end_time)

list1 = [54,26,93,17,77,31,44,55,20]
start = default_timer()
alist=mergeSort(list1)
end_time=default_timer() - start

print "The time for merge sort is "+ str(end_time)
