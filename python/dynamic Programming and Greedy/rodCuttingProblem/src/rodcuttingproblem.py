# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

'''
A special rod-cutting machine enables a worker to break a rod
into two pieces. This operation costs n time units to break a rod of length n into two pieces.
Suppose a worker wants to break a rod into many pieces by cutting it at different break
points. The order in which the breaks occur can affect the total amount of time used. For
example, suppose that the worker wants to break a 20 units rod into 3 pieces by cutting it at
2 units and 10 units from one end of the rod. If he performs the breaks in left-to-right order,
then the first break costs 20 time units, the second break costs 18 time units (breaking the
rod from 3 units to 20 units), and the third break costs 12 time units, totaling 50 time units.
If he performs the breaks to occur in right-to-left order, however, then the first break costs
20 time units, the second break costs 10 time units, and the third break costs 8 time units,
totaling 38 time units.
Design an algorithm that, given a rod R of length n and an array L[1 : : : m] containing
the break points, computes the lowest cost for a sequence of breaks, as well as the sequence
of breaks. The running time should be polynomial in m
'''
import sys
import copy
__author__ = "Deepanshu Lulla <deepanshu.lulla@gmail.com>"
__date__ = "$Feb 23, 2017 9:31:02 AM$"

class Rod:
    def __init__(self,start=0,end=0):
        if end<start or end<0 or start <0:
            raise Exception("Scale can't be of length less than 0")
        self.start=start
        self.end=end
    def length(self):    
        return self.end-self.start
       

class Solution:
    def __init__(self):
        self.cost=0
        self.seq=dict()
    
    def value(self,arr,startIndex,endIndex):
        resArray=self.allpermutationsOfArray(arr)
        minval=self.minCost2(arr,startIndex,endIndex)
        resDict=dict()
        for res in resArray:
            #print minval,res
            #print res
            self.seq[str(','.join(res))]=minval
            minval=min(minval,self.minCost2(res,startIndex,endIndex))
            
            
        return minval
        
    def allpermutationsOfArray(self,arr):
        if len(arr) == 1:
          return [arr]
        result = []
        for index, letter in enumerate(arr):
          arr2=copy.copy(arr)
          arr2.pop(index)
          #print list(elem for elem in allpermutationsOfArray(arr2))
          result = result + [[letter] + elem for elem in self.allpermutationsOfArray(arr2)]
          #print letter,result
        return result
    def minCost(self,arr,rod):
        #the values in cutArray are coordinates where the cut is going to take place
        #nl=0
        #r=Rod(0,self.rl)
        #nl=copy.copy(self.rl)
        #cost=0
        i=0
        
        while len(arr)>=1:
            if rod.length()<arr[i]:
                return 0
            elif arr[i]==min(arr):
                self.cost+=rod.length()
                
                #print arr,self.cost
                rod.start=arr[i]
                
                arr.pop(i)
                self.minCost(arr,rod)
            elif arr[i]==max(arr):
                self.cost+=rod.length()
                #print arr,self.cost
                rod.end=arr[i]
                arr.pop(i)
                self.minCost(arr,rod)
            elif min(arr)<arr[i] and arr[i]<max(arr):
                self.cost+=rod.length()
                rod1=Rod(rod.start,arr[i])
                rod2=Rod(arr[i],rod.end)
                #print arr,self.cost
                arr.pop(i)
                print ("Creating new rod with start as %d and end as %d"%(rod1.start,rod1.end))
                self.minCost(arr,rod1)
                print ("Creating new rod with start as %d and end as %d"%(rod2.start,rod2.end))
                self.minCost(arr,rod2)
                
           #print arr[i],nl,cost
            
            
        return self.cost
    
 
    def minCost2(self,arr,startIndex,endIndex):
        #the values in cutArray are coordinates where the cut is going to take place
        #nl=0
        #r=Rod(0,self.rl)
        #nl=copy.copy(self.rl)
        #cost=0
        i=0
        #print self.cost
        diff=endIndex-startIndex
        while len(arr)>=1:
            if diff<arr[i]:
                return 0
            elif arr[i]==min(arr):
                self.cost+=diff

                #print arr,self.cost
                startIndex=arr[i]

                arr.pop(i)
                self.minCost2(arr,startIndex,endIndex)
            elif arr[i]==max(arr):
                self.cost+=diff
                #print arr,self.cost
                endIndex=arr[i]
                arr.pop(i)
                self.minCost2(arr,startIndex,endIndex)
            elif min(arr)<arr[i] and arr[i]<max(arr):
                self.cost+=diff
                #rod1=Rod(rod.start,arr[i])
                #rod2=Rod(arr[i],rod.end)
                #print arr,self.cost
                temp=copy.copy(arr[i])
                arr.pop(i)
                #print ("Creating new rod with start as %d and end as %d"%(rod1.start,rod1.end))
                self.minCost2(arr,startIndex,temp)
                self.minCost2(arr,temp,endIndex)
                #print ("Creating new rod with start as %d and end as %d"%(rod2.start,rod2.end))


           #print arr[i],nl,cost


            return self.cost
    
        
if __name__ == "__main__":
    s=Solution()
    s1=Solution()
    s2=Solution()
    r=Rod(0,20)
    print s.minCost([10,8,2],r)
    #cost=0
    print s1.value([10,8,2],0,20),s1.seq
    
    