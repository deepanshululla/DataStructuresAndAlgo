def seqSearch(list1,item):
	l=len(list1)
	found=False
	stop=False
	for i in range(0,l):
		if list1[i]==item and not found and not stop:
			print("item found at position ",i)
			found=True
			
		else:
			if list1[i]>item and not found and not stop:
				print('item not in  list')
				stop=True
	if not found and not stop:
		print('item not in  list')
				
	

def  binSearch(list1,item):
	l=len(list1)
	first=0
	last=l-1
	
	found=False
	while first<=last and not found:
		mid_value=(first+last)//2
		if item==list1[mid_value]:
			print("item found")
			found=True
		else:
			if item<list1[mid_value]:
				last=mid_value-1
			else:
				first=mid_value+1
				
	return found

	
	
def  binSearch2(list1,item):
	l=len(list1)
	first=0
	last=l-1
	mid_value=(first+last)//2
	found=False
	if l==0:
		return False
	else:
		if item==list1[mid_value]:
			print("item found")
			#found=True
			return True
		else:
			if item<list1[mid_value]:
				binSearch2(list1[:mid_value],item)
			else:
				binSearch2(list1[mid_value+1:],item)
				
		
def main():
	#seqSearch([1,3,5],5)
	k=binSearch2([1,2,3,5,6],3)
	print(k)
main()