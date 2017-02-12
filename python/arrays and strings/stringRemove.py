def removeChars(string,str2remove):
	list=[]
	for i in range(len(string)):
		if string[i] not in str2remove:
			list.append(string[i])
		else:
			pass
			
	return ''.join(list)

print removeChars('This function has no name. It returns a function object which is assigned to the identifier double. We can now call it as a normal function.','aeiou')	