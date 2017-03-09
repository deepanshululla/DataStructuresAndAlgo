# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Deepanshu Lulla <deepanshu.lulla@gmail.com>"
__date__ = "$Mar 4, 2017 10:47:30 PM$"
import sys

class StockPrices:
    def __init__(self,arr):
        self.arr=arr
        self.maxdiff=0
        if len(arr)<2:
            raise Exception("we need to have atleast two prices to make profit")
    def method1(self):
        #greedy approach
        #runs in O(n),constant space
        #assumes only one transaction is possible
        minVal=sys.maxint
        minIndex=0
        maxVal=-sys.maxint
        maxIndex=0
        for i in range(len(self.arr)):
            if self.arr[i]<minVal:
                minVal=self.arr[i]
                minIndex=i
            if self.arr[i]>maxVal and i>minIndex:
                maxVal=self.arr[i]
                maxIndex=i
        sol=maxVal-minVal
        if maxIndex<minIndex:
            print "It seems there is no way to earn profit as stocks fell thoughout"
        else:
            print "buy on day %d and sell on day %d"%(minIndex,maxIndex)
        if sol<0:
            return 0
        
        
        return sol
    def method2(self,start,end):
        #divide and conquer approach, time=O(nlogn), space =O(1)
        #assumes only one transaction is possible
        if start>=end:
            return 0
        if end-start==1:
            diff=self.arr[end-1]-self.arr[start]
            if diff>0:
                return diff
            else:
                return 0
        #print start,end
        mid=(start+end)/2
        #lefthalf=self.arr[start:mid]
        #righthalf=self.arr[mid:end]
        m1=self.method2(start,mid)
        m2=self.method2(mid,end)
        v1=min(self.arr[start:mid])
        v2=max(self.arr[mid:end])
        #print (m1,m2,v2-v1)
        return max(m1,m2,v2-v1)
    
    def method3(self,numTransactions):
        '''
        #the difference here is we are introducing another variable k which 
        #indicates the max no. of times we can do stock trade.
        #Subproblem: profit[t][d]=max(profit[t][d-1],argmax(price[t]-price[m]+profit[t-1][j]) for all m from 0 to t-1)
        #profit[t][d]= maximum profit with t transactions uptil and inlcuding day d
        #t=transactons,d=days
        #the left expression when he doesn't tade on that day,the right one is buying shares on mth day 
        #and selling shares on jth day + max profit until last day
        # t is no. of transactions i is no. of day
        '''
        numDays=len(self.arr)
        profit=[[0 for x in range(numDays+1)] for y in range(numTransactions+1)]
        #creating an array of numDays*numTransactions
        #basecases are already included
        #but basecases are if numDays are 0 profit =0,if numTransactions are 0 profit =0
        for j in range(1,numTransactions+1):
            for i in range(1,numDays):
            
                maxVal=-sys.maxint
                for m in range(0,i):
                    maxVal=max(maxVal,self.arr[i]-self.arr[m]+profit[j-1][m])
                noTran=profit[j][i-1]#assuming he doesn't do any transaction on ith day
                tran=maxVal#assuming transaction is done on ith day
                profit[j][i]=max(tran,noTran)
        #print profit        
        return profit[numTransactions][numDays-1] 
    
if __name__ == "__main__":
    stock_prices_yesterday = [6, 10, 7, 5, 8, 11, 9]
    s=StockPrices(stock_prices_yesterday)
    print s.method1()
    #print s.method2(0,len(stock_prices_yesterday))
    s=StockPrices([10, 22, 5, 75, 65, 80])
    print s.method3(2)
    s=StockPrices(stock_prices_yesterday)
    print s.method3(1)
    '''
    stock_prices_yesterday = [10,9, 7, 5, 2]
    s=StockPrices(stock_prices_yesterday)
    print s.method1()
    print s.method2(0,len(stock_prices_yesterday))
    stock_prices_yesterday = [10,10,10,10,10,10]
    s=StockPrices(stock_prices_yesterday)
    print s.method1()
    print s.method2(0,len(stock_prices_yesterday))
    print "Hello World"
    '''