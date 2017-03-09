'''
Given a gold mine of n*m dimensions. Each field in this mine contains a positive integer which is the amount of gold in tons. 
Initially the miner is at first column but can be at any row. He can move only (right->,right up /,right down\)
that is from a given cell, the miner can move to the cell diagonally up towards
the right or right or diagonally down towards the right. Find out maximum amount of gold he can collect.

Examples:

Input : mat[][] = {{1, 3, 3},
                   {2, 1, 4},
                  {0, 6, 4}};
Output : 12 
{(1,0)->(2,1)->(2,2)}

Input: mat[][] = { {1, 3, 1, 5},
                   {2, 2, 4, 1},
                   {5, 0, 2, 3},
                   {0, 6, 1, 2}};
Output : 16
(2,0) -> (1,1) -> (1,2) -> (0,3) OR
(2,0) -> (3,1) -> (2,2) -> (2,3)

Input : mat[][] = {{10, 33, 13, 15},
                  {22, 21, 04, 1},
                  {5, 0, 2, 3},
                  {0, 6, 14, 2}};
Output : 83
'''
import sys

__author__ = "Deepanshu Lulla <deepanshu.lulla@gmail.com>"
__date__ = "$Mar 7, 2017 2:51:39 PM$"

class GoldMine:
    
    def __init__(self,mat):
        if mat and isinstance(mat,list):
            self._gold_arr=mat
            self._path=[]
        else:
            raise Exception("value error for mat array")
    def _max_profit(self,row,col):    
        '''
        arguments
        row,col
        returns
        maxAmount of gold that can be collected
        raises Error 
        fs row,col is not integer or row,col <0 or row!=len(self.arr)
        '''
        if row<0 or col<0:
            raise Excetion("index error")
        if type(row) is not int and type(col) is not int:
            raise Exception("value Error for row and col")
      
        table=[[0 for x in range(row)] for y in range(col)]
        for i in range(col-1,-1,-1):
            for j in range(row):
                #Gold collected on going to the cell on the right(->)
                right=0 if (i==col-1) else table[j][i+1]
                #Gold collected on going to the cell on the rightUp(/)
                right_up= 0 if(j==0 or i==col-1) else table[j-1][i+1]
                #Gold collected on going to the cell to right down (\)
                right_down=0 if (i==col-1 or j==row-1) else table[j+1][i+1]
                #maxGold
                if right>right_up and right>right_down:
                    self._path.append([j,i+1])
                elif right_up>right and right_up>right_down:
                    self._path.append([j-1,i+1])
                elif right_down>right and right_up<right_down:
                    self._path.append([j+1,i+1])
                table[j][i]=self._gold_arr[j][i]+max(right,right_up,right_down)
                #self._path.append([j,i])
        #print table
        #print self._path
        res=-sys.maxint
        # The max amount of gold collected will be the max
        # value in first column of all rows
        for j in range(row):
            
            res=max(res,table[j][0])
        return res    
        
                
if __name__ == "__main__":
    mat=[[1,3,3],[2,1,4],[0,6,4]]
    s=GoldMine(mat)
    print s._max_profit(3,3)
    
