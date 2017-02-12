def intFromString(string):
	isNeg=False
	if string[0]=='-':
		isNeg=True
	n=len(string)-1
	sum=0	
	if isNeg:
		for i in range(1,n+1):
			sum+=int(string[i])*(10)**(n-i)
			
		sum=-sum	
	else:
		for i in range(0,n+1):
			#print int(string[i])
			sum+=int(string[i])*(10)**(n-i)
	print sum
	return sum		

intFromString('53')
intFromString('-353')
intFromString('0')
intFromString('-1')
intFromString('1')
