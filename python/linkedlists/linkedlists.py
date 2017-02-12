#!/usr/bin/python

class Node:
	def __init__(self,initdata):
		self.data=initdata
		self.next=None
		self.prev=None
		self.index=0
	def getData(self):
		return self.data
	
	def getNext(self):
		return self.next
		
	def getPrev(self):
		return self.prev
	
	def setNext(self,nextNode):
		self.next=nextNode
		
	def setPrev(self,prevNode):
		self.prev=prevNode
	
	def getIndex(self):
		return self.index

class SinglyLinkedList:
	def __init__(self):
		self.head=None
		self.length=0
			
			
	def isEmpty(self):
		return self.head==None
		
	def add(self,item):
		n=Node(item)
		if (self.isEmpty()):
			
			self.head=n
			self.length=1
		else:
			#ADDING NEW ELEMENT TO HEAD OF ARRAY
			#stack implentation
			n.setNext(self.head)
			self.head=n
			self.length+=1
			
	def search(self,item):
		found=False
		current=self.head
		
		for i in  range(0,self.length):
			if found:
				break
			else:
				if current.getData()==item:
					
					found=True
				else:
					current=current.getNext()
			
		return found	

	def remove(self,item):
		found=False
		current=self.head
		previous=None
		for i in  range(0,self.length):
			if found:
				break
			else:
				if current.getData()==item:
					found=True
					temp=current.getNext()
					previous.setNext(temp)
					self.length=self.length-1
				else:
					previous=current
					current=current.getNext()
					
	def printList(self):
		current=self.head
		for i in range(0,self.length):
			print current.getData(),
			current=current.getNext()
		print	

class SinglyLinkedList2:
	def __init__(self):
		self.head=None
		self.tail=None
		self.length=0
		
			
			
	def isEmpty(self):
		return self.head==None
		
	def add(self,item):
		n=Node(item)
		if (self.isEmpty()):
			
			self.head=n
			self.tail=n
			self.length=1
			n.index=0
		else:
			#ADDING NEW LEMENT TO end OF ARRAY
			#queue implement
			n.index=self.length
			#n.setNext("None")
			temp=self.tail
			temp.setNext(n)
			self.tail=n
			self.length+=1
			
	def search(self,item):
		found=False
		current=self.head
		
		for i in  range(0,self.length):
			if found:
				break
			else:
				if current.getData()==item:
					
					found=True
				else:
					current=current.getNext()
			
		return found	

	def remove(self,item):
		found=False
		current=self.head
		previous=None
		for i in  range(0,self.length):
			if found:
				break
			else:
				if current.getData()==item:
					found=True
					temp=current.getNext()
					previous.setNext(temp)
					self.length=self.length-1
				else:
					previous=current
					current=current.getNext()
					
	def printList(self):
		current=self.head
		for i in range(0,self.length):
			print current.getData(),
			current=current.getNext()
		print
		
class DoublyLinkedList:
	def __init__(self):
		self.head=None
		self.tail=None
		self.length=0
		
			
			
	def isEmpty(self):
		return self.head==None
		
	def add(self,item):
		n=Node(item)
		if (self.isEmpty()):
			
			self.head=n
			self.head.setNext(self.tail)
			
			self.tail=n
			self.tail.setPrev(self.head)
			self.length=1
			n.index=0
		else:
			#ADDING NEW LEMENT TO end OF ARRAY
			#queue implement
			n.index=self.length
			#n.setNext("None")
			
			self.tail.setNext(n)
			n.setPrev(self.tail)
			self.tail=n
			self.length+=1
			
	def search(self,item):
		found=False
		current=self.head
		
		for i in  range(0,self.length):
			if found:
				break
			else:
				if current.getData()==item:
					
					found=True
				else:
					current=current.getNext()
			
		return found	

	def remove(self,item):
		found=False
		current=self.head
		previous=None
		for i in  range(0,self.length):
			if found:
				break
			else:
				if current.getData()==item:
					found=True
					temp=current.getNext()
					previous.setNext(temp)
					temp.setPrev(previous)
					self.length=self.length-1
				else:
					previous=current
					current=current.getNext()
					
	def printList(self):
		current=self.head
		for i in range(0,self.length):
			print current.getData(),
			current=current.getNext()
		print
			
		
	
def testSingleLinkedList():		
	l=DoublyLinkedList()
	l.add(45)
	l.add('cat')
	l.add(-24)
	l.add(-24)
	l.add(-26)
	l.add('foo')
	l.add(3)
	l.add(4)
	l.printList()
	l.remove(-26)
	l.printList()
	print(l.search('cat'))
	print(l.search('cat1'))
	print(l.search(4))

testSingleLinkedList()	
