#https://www.hackerrank.com/contests/bits-goa-day-3/challenges/knapsack-problem
#implementation of 10 knapsack or discrete knapsack
__author__ = "Deepanshu Lulla <deepanshu.lulla@gmail.com>"
__date__ = "$Feb 17, 2017 10:59:41 AM$"
class StoreInput:
    def __init__(self):
        [s,n]=raw_input().split()
        self.bagCap=int(s)
        self.numItems=int(n)
        self.valueArray=[0 for x in range(self.numItems)]
        self.weightArray=[0 for x in range(self.numItems)]
        for i in range(0,self.numItems):
            valueS,weightS=raw_input().split()
            self.valueArray[i]=int(valueS)
            self.weightArray[i]=int(weightS)

class Item:
    #creating a datastructure that has two parts value and weight
    def __init__(self,index,value,weight):
        self.value=value
        self.weight=weight
        if weight>0:
            self.quality=float(value)/weight
        else:
            self.quality=0.0
        self.used=0
        self.index=index
        
class ItemList:
    #data structure for list of items
    def __init__(self,numItems,weightArr,valueArr):
        self.itemList=[None for item in range(numItems)]
        for i in range(numItems):
            it=Item(i,weightArr[i],valueArr[i])
            self.itemList[i]=it
           




def discreteKnapsack(itemList,maxweight,numItems):
    #this can not be solved by greedy
    #we need to create an optimal substructure for this for doing this with dynamic programming
    #we will create a table for storing maxvalues with maxweight+1 rows and numItems+1 coloums
    #There are only two conditions whether we choose an item or we don't
    #hence maximum value can be achieved by finding max(when element was chosen,when it wasn't)
    #bottom up
    #mergeSortBasedOnQuality(itemList)
    #itemList.reverse()
    
    table=[[0 for x in range(maxweight+1)] for x in range(numItems+1)]
    for i in range(0,numItems+1):
        for w in range(0,maxweight+1):
            if i>0 and w>0:
                index=i-1
                #print index
                if itemList[index].weight<=w:
                    #this is saying if our itemList weight < than the weight row
                    part1=itemList[index].value+table[i-1][w-itemList[index].weight]
                    part2=table[i-1][w]
                    #optimal substructure. In part 1 we are using the value In part 2 we aren't
                    table[i][w]=max(part1,part2)
                else:
                    #this is saying to not use that item
                    table[i][w]=table[i-1][w]
        #print itemList[i-1].quality        
    #print table            
    return table[numItems][maxweight]               

def discreteKnapsack2(itemList,maxweight,numItems):
    #this can not be solved by greedy
    #we need to create an optimal substructure for this for doing this with dynamic programming
    #There are only two conditions whether we choose an item or we don't
    #hence maximum value can be achieved by finding max(when element was chosen,when it wasn't)
    #top down
    if numItems==0:
        return 0
    if maxweight==0:
        return 0
    l=numItems
    if itemList[l-1].weight>maxweight:
        return discreteKnapsack2(itemList,maxweight,numItems-1)
    else:
        part1=itemList[l-1].value+discreteKnapsack2(itemList,maxweight-itemList[l-1].weight,numItems-1)
        part2=discreteKnapsack2(itemList,maxweight,numItems-1)
        return max(part1,part2)
    
           
    

if __name__ == "__main__":
    #our task here is to maximize overAll value we are carrying  but not exceed bag Capacity
    inp=StoreInput()
    itemListObj=ItemList(inp.numItems,inp.weightArray,inp.valueArray)
    d=discreteKnapsack(itemListObj.itemList,inp.bagCap,inp.numItems)
    print d
    
