# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Deepanshu Lulla <deepanshu.lulla@gmail.com>"
__date__ = "$Feb 23, 2017 11:30:11 AM$"
#the goal is to compute C(n,r) and P(n,r)

class Combinations:
    def __init__(self):
        self.choices=[]
        
    def numChoose(self,n,r):
        #the order of items don't matter#assuming distinct elements
        #basically calculating C(n,r)
        arr=[[0 for x in range(r+1)] for y in range(n+1)]
        for i in range(0,n+1):
            arr[i][0]=1
        for j in range(0,r+1):
            arr[0][r]=0
        for i in range(1,n+1):
            for j in range(1,r+1):
                if i==j:
                    arr[i][j]=1
                elif i<j:
                    arr[i][j]=0
                else:
                    arr[i][j]=arr[i-1][j-1]+arr[i-1][j]
        return arr[n][r]
        
    def numPermutate(self,n,r):
        #the order of items don't matter#assuming distinct elements
        #basically calculating C(n,r)
        arr=[[0 for x in range(r+1)] for y in range(n+1)]
        for i in range(0,n+1):
            arr[i][0]=1
        for j in range(0,r+1):
            arr[0][r]=0
        for i in range(1,n+1):
            for j in range(1,r+1):
                if i==j:
                    arr[i][j]=j*arr[i-1][j-1]
                elif i<j:
                    arr[i][j]=0
                else:
                    arr[i][j]=j*arr[i-1][j-1]+arr[i-1][j]
        return arr[n][r]

class Solution:
    def permutate(self,n,r,str1):
        # we need to choose r objects out of n objects and then find out permutation of each of them
        #For eg choose from {A,B,C} AB,BC,CA now permuations of AB are {AB,BA} .Similarly for BC,CA. hence num of permutaions =C(n,r)*r!=P(n,r)
        #Permutation of {A,B,C,D] choosing 3 at a time C(4,3)=4. Number of ways 3 elements can be rearranged=3!=6. Answer=24
        cObj=Combinations()
        C=cObj.numChoose(n,r)
        #randStr=''.join([str(i) for i in range(1,r+1)])
        nObj=NumRearangements(str1)
        N=nObj.value(0,r-1)
        print C,N
        print cObj.numPermutate(n,r)
        return C*N
    

class NumRearangements:
    def __init__(self,str1='',lst=[]):
        self.count=0
        if lst is []:
            self.arr=list(str1)
            self.l=len(self.arr)
        elif str is '':
            self.arr=lst
            self.l=len(self.arr)
        else:
            raise Exception("Invalid parameters")
        
    def value(self,startIndex,endIndex):
        #computes no. of rearrangements of r items=r!
        #r=endIndex-startIndex+1
        
        if startIndex>=endIndex:
            self.count+=1
        else:
            for i in xrange(startIndex,endIndex):
                self.arr[startIndex],self.arr[i]=self.arr[i],self.arr[startIndex]
                self.count+=1
                self.value(startIndex+1,endIndex)
                self.arr[startIndex],self.arr[i]=self.arr[i],self.arr[startIndex]#backtrack
        return self.count       
    
            

    
    
if __name__ == "__main__":
    seq="ABCDEFGI"
    n=len(seq)
    #n=5
    r=2
    s=Solution()
    n=NumRearangements([2,8,10])
    n.value(0,2)
    print s.permutate(n,r,seq)
    
