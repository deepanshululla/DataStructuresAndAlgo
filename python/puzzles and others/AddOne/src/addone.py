# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Deepanshu Lulla <deepanshu.lulla@gmail.com>"
__date__ = "$Feb 18, 2017 11:25:59 AM$"

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        Aint=int(self.convertToString(A))
        B=Aint+1
        arr=self.convertToArray(str(B))
        return arr        
    def convertToString(self,A):
        str1=''
        for i in range(0,len(A)):
            elemS=str(A[i])
            str1+=elemS
        return str1
    def convertToArray(self,Astring):
        #inp=reversed(Astring)
        arr=[]
        #print len(Astring)
        for elem in Astring:
            #print int(elem)
            arr.append(int(elem))
        return arr
    
if __name__ == "__main__":
    #print "Hello World"
    s=Solution()
    arr=s.plusOne([0,9,9,9,0])
    print arr