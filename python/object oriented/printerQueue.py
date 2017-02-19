import random
from queue import Queue

class Printer:
	def __init__(self,ppm):
		self.pagerate=ppm;
		self.currenttask=None;
		self.timeremaining=0;
		
	def tick(self):
		if self.currenttask!=None:
			self.timeremaining=self.timeremaining-1;
			if self.timeremaining<0:
				self.currenttask=None
				
	def busy(self):
		if self.currenttask!=None:
			return True;
		else:
			return False;
	
	def startNext(self,nextTask):
		self.currenttask=nextTask;
		self.timeremaining=nextTask.getPages()* 60/self.pagerate;
		
		
class Task:
	def __init__(self,time):
		self.timestamp=time;
		self.pages=random.randrange(1,21)
	def getPages(self):
		return self.pages
	def getStamp(self):
		return self.timestamp
	def waitTime(self,currentTime):
		return currentTime-self.timestamp
		
def simulation(numSeconds,pagesPerMinute):
	labPrinter=Printer(pagesPerMinute);
	printQueue=Queue();
	waitingTimes=[]
	
	for currentSecond in range(numSeconds):
		if newPrintTask():
			task=Task(currentSecond)
			printQueue.enqueue(task)
		if (not labPrinter.busy()) and (not printQueue.isEmpty()):
			nextTask=printQueue.dequeue()
			waitingTimes.append(nextTask.waitTime(currentSecond))
			labPrinter.startNext(nextTask)
			
		labPrinter.tick()
	averageWait=sum(waitingTimes)/len(waitingTimes)
	print("Average wait %6.2f seconds and %3d tasks remaiing"%(averageWait,printQueue.size()))

		

def newPrintTask():
	num = random.randrange(1,181)
	if num == 180:
		return True
	else:
		return False
		

for i in range(10):
	simulation(3600,5)
	