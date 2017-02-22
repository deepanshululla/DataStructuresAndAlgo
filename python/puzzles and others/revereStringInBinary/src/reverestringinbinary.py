'''

Task
Your task will be to write a program for reversing numbers in binary. For instance, 
the binary representation of 13 is 1101, and reversing it gives 1011, which corresponds to number 11.

Input
The input contains a single line with an integer N, 1 ? N ? 1000000000.

Output
Output one line with one integer, the number we get by reversing the binary representation of N.

Sample input 1
13
Sample output 1
11
Sample input 2
47
Sample output 2
61
 
'''

__author__ = "Deepanshu Lulla <deepanshu.lulla@gmail.com>"
__date__ = "$Feb 20, 2017 8:02:30 PM$"

class Solution:
    def __init__(self,num):
        self.num=int(num)
      
    def createBinaryString(self,n):
        return "{0:b}".format(n)
    
    def reverseString(self,s):
        return s[::-1]
    
    def convertBinaryStringToDecimal(self,numS):
        return int(numS,2)
    def finalResult(self):
        return self.convertBinaryStringToDecimal(self.reverseString(self.createBinaryString(self.num)))
    
        
if __name__ == "__main__":
    m=raw_input()
    if m is not None:
        m=int(m)
        s=Solution(m)
        print s.finalResult()
    #print "Hello World"
