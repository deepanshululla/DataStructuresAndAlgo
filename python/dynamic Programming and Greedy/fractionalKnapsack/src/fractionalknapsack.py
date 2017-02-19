# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
__author__ = "Deepanshu Lulla <deepanshu.lulla@gmail.com>"
__date__ = "$Feb 16, 2017 6:29:43 PM$"

'''
Input:
  Items as (value, weight) pairs
  arr= [[60, 10], [100, 20], [120, 30]]
  Knapsack Capacity, W = 50;
Output:
   Maximum possible value = 240
   By taking full items of 10 kg, 20 kg and 
   2/3rd of last item of 30 kg
'''
class Item:
    #creating a datastructure that has two parts value and weight
    def __init__(self,name,value,weight):
        self.value=value
        self.weight=weight
        self.quality=value/weight
        self.used=0
        self.name=name
        
class ItemList:
    #data structure for list of items
    def __init__(self,arr):
        self.itemList=[None for item in range(len(arr))]
        for i in range(0,len(self.itemList)):
            it=Item(arr[i][0],arr[i][1],arr[i][2])
            self.itemList[i]=it
       
def mergeSortBasedOnQuality(itemList):
    length=len(itemList)
    if length>1:	
            mid=length//2
            leftHalf=itemList[:mid]
            rightHalf=itemList[mid:]
            mergeSortBasedOnQuality(leftHalf)
            mergeSortBasedOnQuality(rightHalf)
            l1=len(leftHalf)
            l2=len(rightHalf)		
            i=0
            j=0
            k=0
            while i<l1 and j<l2:
                    if leftHalf[i].quality<rightHalf[j].quality:
                            itemList[k]=leftHalf[i]
                            i=i+1
                    else:
                            itemList[k]=rightHalf[j]
                            j=j+1
                    k=k+1
            while i<l1:
                    itemList[k]=leftHalf[i]
                    i=i+1
                    k=k+1

            while j<l2:
                    itemList[k]=rightHalf[j]
                    j=j+1
                    k=k+1
      

def fractionalKnapsack(itemListObj,maxWeight,lenArray):
    #used greedy approach to solve this by first sorting base don quality
    currentWeight=0
    currentValue=0
    mergeSortBasedOnQuality(itemListObj.itemList)
    itemListObj.itemList.reverse()
    for item in itemListObj.itemList:
        if currentWeight+item.weight<maxWeight:
            currentWeight+=item.weight
            currentValue+=item.value
            item.used=item.weight
        else:    
            remaining=maxWeight-currentWeight
            currentValue+=(item.value*remaining)/item.weight
            item.used=remaining
            break
    return [currentValue,itemListObj]

if __name__ == "__main__":
    arr= [['rice',60, 10], ['wheat',100, 20], ['sugar',120, 30],['salt',20,20],['gold',500,20]];
    maxWeight=50
    itemListObj=ItemList(arr)
    finalValue,itemListObj2=fractionalKnapsack(itemListObj,maxWeight,len(arr))
    print "The final max value is %d" %finalValue
    print("Quantities used")
    for item in itemListObj2.itemList:
        print('%s=%d'%(item.name,item.used))
    
