# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Deepanshu Lulla <deepanshu.lulla@gmail.com>"
__date__ = "$Feb 21, 2017 9:35:25 PM$"
import math


class TwoEggs:
    def __init__(self,numFloors,breakFloor):
        self.answer=breakFloor
        self.numFloors=numFloors
        
    def __linearSearch(self,si,ei):
        if ei==0:
            return 0
        if si==100:
            return 100
        elif (ei>si and ei>0 and si>=0):
            print
            print "Second Egg tested on",
            for i in range(si,ei+1):
                print i,
                if (self.__breaksOrNot(i)):
                    print
                    return i
        
                    #break
    
    def findFloor1(self):
        num=self.numFloors/2
        print("First egg tested on floor "+str(num) )
        if (self.__breaksOrNot(self.numFloors/2)):
            
            sol=self.__linearSearch(0,self.numFloors/2-1)
        else:
            sol=self.__linearSearch(self.numFloors/2,self.numFloors)
        return sol
    
    def findFloor2(self):
        N=self.numFloors
        i=0
        print "Dropping egg 1 from floors ",
        skipPoint=int((1+math.sqrt(1+8*N))/2)
        while (i<=N and i>=0):
            print str(i),
            if(self.__breaksOrNot(i)):
                return self.__linearSearch(i-skipPoint,i)
            else:
                i+=skipPoint
                if i>0:
                    skipPoint-=1
                
                
            
   
        
if __name__ == "__main__":
    s=TwoEggs(1000,500)
    print "The answer is "+ str(s.findFloor2())
    
    
class EggDropGeneral:
    def __init__(self,numFloors,numEggs,answer):
        self.numFloors=numFloors
        self.numEggs=numEggs
        self.answer=answer
        self.__memo={}
        
    def result(self):
        
        return
    def __linearSearch(self,si,ei):
        if ei==0:
            return 0
        if si==100:
            return 100
        elif (ei>si and ei>0 and si>=0):
            print
            print "Second Egg tested on",
            for i in range(si,ei+1):
                print i,
                if (self.__breaksOrNot(i)):
                    print
                    return i
                
    def __breaksOrNot(self,numFloor):
        if numFloor>=self.answer:
            return True
        else:
            return False
        