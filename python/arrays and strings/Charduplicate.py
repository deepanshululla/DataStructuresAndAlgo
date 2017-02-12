#!/usr/bin/python


class DupChar:
	def __init__(self,string):
		self.str=string
		self.list=[]
		self.hashmap={}
	def findfirstUndupChar(self):
		
		for i in range(0,len(self.str)):
			if self.str[i] not in self.hashmap.keys():
				self.hashmap[self.str[i]]=1
				self.list.append(self.str[i])
			else:
				self.hashmap[self.str[i]]+=1
				
				self.list.remove(self.str[i])
				
		print self.list[0]
	
		def findfirstUndupChar(self):
		
			for i in range(0,len(self.str)):
				if self.str[i] not in self.hashmap.keys():
					self.hashmap[self.str[i]]=1
					self.list.append(self.str[i])
				else:
					self.hashmap[self.str[i]]+=1
					
					self.list.remove(self.str[i])
					
			print self.list[0]	
	
	
if __name__=="__main__":
		a1=DupChar('total')
		a1.findfirstUndupChar()
		a2=DupChar('teeth')
		a2.findfirstUndupChar()
		