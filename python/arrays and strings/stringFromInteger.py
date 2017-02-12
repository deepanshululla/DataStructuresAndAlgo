def stringFromInt(num):
	isNeg=False
	temp=''
	n=0
	if num<0:
		isNeg=True
		num=-num
		
	i=0
	while(num>=0):
		n=num%10
		c=str(n);
		temp+=c
		i+=1
		num/=10
		if num==0:
			break
	if isNeg:
		temp+='-'
	print temp[::-1]

stringFromInt(01241)
print int(1241)
#stringFromInt(2000)
