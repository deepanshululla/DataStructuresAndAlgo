# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Deepanshu Lulla <deepanshu.lulla@gmail.com>"
__date__ = "$Mar 2, 2017 9:15:10 PM$"
class Solution:
    def __init__(self,arr1,arr2):
        
        if arr1 is []:
            return arr2
        if arr2 is []:
            return arr1
        
        newList=[]
        i=0
        j=0
        k=0
        while i<len(arr1) and j <len(arr2):
            if arr1[i]<=arr2[j]:
                newList.append(arr1[i])
                i=i+1
            else:
                newList.append(arr2[j])
                j=j+1
            k+=1
        while i<len(arr1):
            newlist.append(arr1[i])
            i+=1
            k+=1
        while j<len(arr2):
            newList.append(arr2[j])
            j+=1
            k+=1
        self.newList=newList
    def returnList(self):
        return self.newList
    

if __name__ == "__main__":
    #print "Hello World"
    my_list     = [3, 4, 6, 10, 11, 15]
    alices_list = [1, 5, 8, 12, 14, 19]
    s=Solution(my_list,alices_list)
    print s.returnList()