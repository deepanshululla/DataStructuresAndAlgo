str1="there is a string"
str11=str1
str2=''
list1=str1.split(' ')
#print list
l=len(list1)
for i in range(l):
	str2=str2+list1[l-i-1]+' '
	
print str2
list2=str1.split(' ')
list2.reverse()
str3=' '.join(list2)
#str3=' '.join(str1.split().reverse())
print str3

str4=' '.join(str1.split(' ')[::-1])
print ' '.join(str1.split(' ')[::-1])