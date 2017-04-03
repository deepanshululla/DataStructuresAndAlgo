#!/usr/bin/python

#This is file with binary tree implementation


class BinaryTree:
	#we don't need Node class for binary tree. It was implemented for Tree
	def __init__(self,root):
		
		self.root=root
		self.leftChild=None
		self.rightChild=None
		
	def insertLeft(self,item):
		if self.leftChild == None:
			self.leftChild=BinaryTree(item)
		else:
			t=BinaryTree(item)
			t.leftChild=self.leftChild
			self.leftChild=t
	
	def insertRight(self,item):
		if self.rightChild == None:
			self.rightChild=BinaryTree(item)
		else:
			t=BinaryTree(item)
			t.rightChild=self.rightChild#every child is a tree
			self.rightChild=t
	
	def getLeftChild(self):
		return self.leftChild
	
	def getRightChild(self):
		return self.rightChild
	
	def getRootVal(self):
		return self.root
		
	def setRootVal(self,item):
		self.root=item
	def preOrderPrint(self):
		# Process t# Process left sub tree# Process right sub tree
		
		print self.root,
		if self.leftChild:
			self.leftChild.preOrderPrint()
		if self.rightChild:
			self.rightChild.preOrderPrint()
				
	def inOrderPrint(self):
		# Process left sub tree# Process t# Process right sub tree
		if self.leftChild:
			self.leftChild.inOrderPrint()
		print self.root,	
		if self.rightChild:
			self.rightChild.inOrderPrint()	
		
	def postOrderPrint(self):
		# Process left sub tree# Process right sub tree# Process t
		if self.leftChild:
			self.leftChild.postOrderPrint()
		
		if self.rightChild:
			self.rightChild.postOrderPrint()	
		print self.root,
			
	def height(self):
		#finds height/depth of tree
		path=0
		pathleft=0
		pathright=0
		while self.leftChild!=None:
			pathleft+=1
			self=self.leftChild
		while self.rightChild!=None:
			pathright+=1	
			self=self.rightChild
			
		return 1+max(pathleft,pathright)
		
	def levelOrderPrint(self):	
		#this is the bfs print
		
		queue=[]
		currentTree=None
		queue.append(self)
		print "Inorder print"
		while len(queue)>0:
			print queue[0].root,
			current=queue.pop(0)
			if current.leftChild!=None:
				queue.append(current.leftChild)
			if current.rightChild!=None:
				queue.append(current.rightChild)		
		print
	
	def convertToList(self):
		queue=[]
		list=[]
		currentTree=None
		queue.append(self)
		print "Inorder print"
		while len(queue)>0:
			#print queue[0].root,
			list.append(queue[0].root)
			current=queue.pop(0)
			if current.leftChild!=None:
				queue.append(current.leftChild)
			if current.rightChild!=None:
				queue.append(current.rightChild)
			
					
		print list
		return list
	def printPathsWithSum(self):
		sum=0
		strPath=''
		pathDict=dict()
		queue=[]
		currentTree=None
		queue.append(self)
		print "Inorder print"
		while len(queue)>0:
			print queue[0].root,
			current=queue.pop(0)
			if current.leftChild!=None:
				queue.append(current.leftChild)
			if current.rightChild!=None:
				queue.append(current.rightChild)
				

		
def testBinaryTree():
	'''		1
			/ \
		   /   \
		  /     \
		 2       3
		/ \     /
	   4   5   6
	  /       / \
	 7       8   9
	''' 
	r = BinaryTree(1)
	print(r.getRootVal())
	print(r.getLeftChild())
	r.insertLeft(2)
	print(r.getLeftChild())
	print(r.getLeftChild().getRootVal())
	r.insertRight(3)
	print(r.getRightChild())
	print(r.getRightChild().getRootVal())
	#r.getRightChild().setRootVal('hello')
	print(r.getRightChild().getRootVal())
	r.getLeftChild().insertLeft(4)
	r.getLeftChild().insertRight(5)
	r.getLeftChild().getLeftChild().insertLeft(7)
	r.getRightChild().insertLeft(6)
	r.getRightChild().getLeftChild().insertLeft(8)
	r.getRightChild().getLeftChild().insertRight(9)
	print "Preorder"
	r.preOrderPrint()
	
	print "\ninorder"
	r.inOrderPrint()
	print "\npostOrder"
	r.postOrderPrint()
	print
	print r.height()
	r.levelOrderPrint()
	r.convertToList()
		

		
class Tree:
	def __init__(self,root):
		
		self.root=root
		self.children=[]
	
	def searchNode(self,item):
		found=False
		
	def addChild(self,item):
		#addding item as a child whoose root is node. every child is a tree
		n=Tree(item)
		self.children.append(n)
		
if __name__="__main__":
	testBinaryTree()		
		