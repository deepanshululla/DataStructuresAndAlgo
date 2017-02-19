__author__ = "Deepanshu Lulla <deepanshu.lulla@gmail.com>"
__date__ = "$Feb 17, 2017 11:55:29 AM$"


# Enter your code here. Read input from STDIN. Print output to STDOUT
#Question->https://www.hackerrank.com/challenges/coin-change

class GetInput:
    #used to scan input
    def __init__(self):
        self.amount=0
        #self.denoArray=[]
        self.numDeno=0
    def scan(self):
        [mS,nS]=raw_input().split()
        self.denoArrayString=raw_input().split()
        self.amount=int(mS)
        self.numDeno=int(nS)
        self.denoArray=[0]*self.numDeno
        self.convertToInt();
    def convertToInt(self):
        for i in range(0,self.numDeno):
            self.denoArray[i]=int(self.denoArrayString[i])
            


def countSolutions(amount,numDeno):
    
    #finds the minimum no. of coins required to implment solution
    # we need to find the optimal substructure of the solution
    #if countSolutions returns the number of solutions for a particular amount
    #We will start from the last element in the deno Array although it doesn't matter
    #we can say countSolutions=countSolution(if we choose a particular denomination)+countSolution(if we don't choose a particular     #denomination). Our only choice is to either choose a denomination or not choose it
    #choice of arguments denoArray(array for denominations) doesn't change and doesnt need to be included in the countSolutions
    #if the number of coins wer not infinite we would have taken that into consideration 
    #Running time=O(2^n) where n is amount. Space=O(1)
    if amount==0:
        return 1#if amount is zero then there is only one solution to not include any coin
    elif amount<0:
        return 0#if amount is less than 0,then there is no solution
    elif amount>0 and numDeno<=0:
        return 0;#if amount is >0 but no coins are left then no solution exists
    else:
        #the first countSolutions doesn't take the last element into consideration so numDeno decreases by 1 for it.no change in           #amount
        #the right countSolutions takes it into consideration so amount becomes amount-denoArray[numDeno-1] and no chnage in               #numDeno
        return countSolutions(amount,numDeno-1)+countSolutions(amount-denoArray[numDeno-1],numDeno);
       
def countSolutionsFaster(amount,numDeno):
    #there are two problems with the above method. Firstly there are lot of overlapping solutions which means we are repeating
    #lot of subproblems that we already solved. To deal with this we will use a table to store values
    # we will be creating a table with amount on Y axis and numDeno on X axis
    #For it we will create a multidimensional array of numDeno coloumns*(amount+1) rows
    #running time =O(n^2) space=O(n^2)
    table=[[0 for x in range(numDeno)] for x in range(amount+1)]
    #create a table of all 0s
    for j in range(0,numDeno):
        table[0][j]=1
        #for all cases where amount=0 there is only 1 way to select coins i.e choose no coin empty set
        
    for i in range(1,amount+1):
        for j in range(0,numDeno):
            if (i-denoArray[j])>=0:
                #checking if amount is >denomination
                #rightPart=takes a particular denomination into consideration so amount becomes amount-denoArray[numDeno-1] and no                 #change in numDeno
                rightPart=table[i-denoArray[j]][j]
            else:
                rightPart=0
            if j>=1:
                #checking if any denominatiuons left
                #leftPart doesn't take the last element into consideration so numDeno decreases by 1 for it.no change in                           #amount
                leftPart=table[i][j-1]
            else:
                leftPart=0
                
            table[i][j]=leftPart+rightPart
    #the last element or the top corner element will be out answer i.e table[amount][numDeno-1]
    #print table
    return table[amount][numDeno-1]

if __name__ == "__main__":        
    inp=GetInput()
    inp.scan()
    denoArray=inp.denoArray
    amount=inp.amount
    numDeno=inp.numDeno

    sol=countSolutionsFaster(amount,numDeno)
    print sol
