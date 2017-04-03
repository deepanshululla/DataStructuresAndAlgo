class MaxHeap:
	def __init__(self,heapType):
		self.heapList=[0]
		self.heapType=heapType
		#could be either min heap or max heap
		self.currentSize=0
	def percUp(self,i):
		if self.type=="min":
			while i//2>0:
				if self.heapList[i]<self.heapList[i//2]:
					self.heapList[i],self.heapList[i//2]=self.heapList[i//2],self.heapList[i]
				i=i//2	
		else:
			while i//2>0:
				if self.heapList[i]>self.heapList[i//2]:
					self.heapList[i],self.heapList[i//2]=self.heapList[i//2],self.heapList[i]
				i=i//2
	def insert(self,item):
		self.heapList.append(item)
		self.currentSize+=1
		percUp(self.currentSize)
	
	def percDown(self,i):
		while (2*i<=
			
	def delMin(self):
		if self.type=='min':
			
		else:
			self.heapList.pop()
			self.currentSize-=1