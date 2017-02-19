'''
Equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes. For example, in an arrya A:

A[0] = -7, A[1] = 1, A[2] = 5, A[3] = 2, A[4] = -4, A[5] = 3, A[6]=0

3 is an equilibrium index, because:
A[0] + A[1] + A[2] = A[4] + A[5] + A[6]

6 is also an equilibrium index, because sum of zero elements is zero, i.e., A[0] + A[1] + A[2] + A[3] + A[4] + A[5]=0

7 is not an equilibrium index, because it is not a valid index of array A.

Write a function int equilibrium(int[] arr, int n); that given a sequence arr[] of size n, returns an equilibrium index (if any) or -1 if no equilibrium indexes exist.
'''


def solution(A):
    # write your code in Python 2.7
    l=len(A)
    if l==1:
        return 0
    else:
        sum=0
        leftSum=0
        sum=sumElementsRange(0,l-1,A)
        for i in range(0,l):
            sum=sum-A[i]
            if sum==leftSum:
                return i
            leftSum+=A[i]
            
        return -1    
        
  
def sumElementsRange(start,end,Array):
    sum=0
    if start<end:
        for i in range(start,end+1):
            if Array[i]>=-2147483648 and Array[i]<=2147483648:
                sum+=Array[i]
    return sum

A=[-7, 1, 5, 2, -4, 3, 0];
print(solution(A))	