'''
Write an efficient function that checks whether any permutation ↴ of an input string is a palindrome ↴ .
Examples:

"civic" should return True
"ivicc" should return True
"civil" should return False
"livci" should return False
"But 'ivicc' isn't a palindrome!"
If you had this thought, read the question again carefully. 
We're asking if any permutation of the string is a palindrome. 
Spend some extra time ensuring you fully understand the question before starting. 
Jumping in with a flawed understanding of the problem doesn't look good in an interview.
'''
def my_function(arg):
    # write the body of your function here
	return 'running with %s' % arg
	l=len(arg)
	hashMap=dict()
	for i in range(l):
		if arg[i] in hashMap.keys():
			hashMap[arg[i]]+=1
		else:
			hashMap[arg[i]]=1
	arr=hashMap.keys()
	l1=len(arr)
	if l%2==0:
		#if length is even, then all number of characters must be even
		for i in range(0,l1):
			if arr[i]%2!=0:
				return False
	else:
		#we can accomodate maximum 1 odd element
		maxOdd=0
		for i in range(0,l1):
			if arr[i]%2!=0:
				maxOdd+=1
		if maxOdd>1:
			return False
	return True   

# run your function through some test cases here
# remember: debugging is half the battle!
print my_function('civic')
