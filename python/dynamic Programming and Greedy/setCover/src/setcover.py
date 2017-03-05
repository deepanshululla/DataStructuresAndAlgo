'''
You are given n subsets S1; S2; : : : ; Sn of k{1..n}, each with an
integer cost c(i). Find the minimum-cost collection of subsets that covers all 
k{1..n} in

'''
'''
This is very similar to the problem where we have to find some elements in an 
array whoose sum is gven
'''

__author__ = "Deepanshu Lulla <deepanshu.lulla@gmail.com>"
__date__ = "$Mar 1, 2017 11:21:12 AM$"

class Set:
    def __init__(self,setArr=[],cost=0):
        self.arr=setArr
        self.cost=cost
        self.subSetArr=[]
    def equals(self,set2):
        arr2=set2.arr
        #cost2=set2.cost
        if len(arr2)!=len(self.arr):
            return False
        arr2.sort()
        self.arr.sort()
        for i in range(len(arr2)):
            if self.arr[i]!=arr2[i]:
                return False
        return True
    
    def isGreaterThan(self,set2):
        arr=self.arr
        if len(arr)>len(set2.arr):
            return True
        return False
        
def union(set1,set2):
    emp=Set()
    emp.arr=set1.arr+set2.arr
    emp.cost=set1.cost+set2.cost
    return emp

def unionArray(setArr):
    emp=Set()
    for set in setArr:
        emp.arr=emp.arr+set.arr
        emp.cost=emp.cost+set.cost
    emp.subSetArr+=setArr    
    return emp

def intersactionSet(set1,set2):
    return list(set(set1.arr) & set(set2.arr))
    
def subSet_sum(setArr,target,partial=[]):
    
    s=unionArray(partial)
    if s.equals(target):
        subSet.append(s)
        print s.arr
    if s.isGreaterThan(target):
        #print s.arr
        return "exceeded"
    for i in range(0,len(setArr)):
        arr=setArr[i]
        remaining=setArr[i+1:]
        subSet_sum(remaining,target,partial+[arr])
    
        
    
    return subSet
subSet=[]
if __name__ == "__main__":
    S1 = Set([1],10)
    S2=Set([2],20)
    S3=Set([3],4)
    S4=Set([4],5)
    S5=Set([5],30)
    S6=Set([1,2,3,4,5],100)
    U=Set([1,2,3,4,5])
    I=Set()
    #print intersactionSet(S1,S6)
    S9=Set([1],10)
    #print S1.equals(S9)
    #print S1.equals(S2)
    #print S1.equals(S6)
    sub=subSet_sum([S1,S2,S3,S4,S5,S6],U)
    for elem in sub:
        print elem.arr,elem.cost,elem.subSetArr
