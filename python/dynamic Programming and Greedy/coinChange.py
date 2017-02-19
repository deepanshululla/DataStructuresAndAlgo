


def recMC(coinValueList,change):
	minCoins=change
	if change in coinValueList:
		return 1
	k=[]
	
	for c in coinValueList:
		if c<=change:
			k.append(c)
	for i in k:
		numCoins=1+recMC(coinValueList,change-i)
		if numCoins<minCoins:
			
			minCoins=numCoins
			
	print(coinCase)
	return minCoins	

def recDC(coinValueList,change,knownResults):
	minCoins=change
	
	if change in coinValueList:
		knownResults[change]=1
		
		return 1
	elif knownResults[change]>0:
		return knownResults[change]
		#print(knownResults[change])
	else:
		k=[]
		for c in coinValueList:
			if c<=change:
				k.append(c)
		for i in k:
			numCoins=1+recDC(coinValueList,change-i,knownResults)
		
			if numCoins<minCoins:
				minCoins=numCoins
				knownResults[change]=minCoins
		return minCoins
			


def myCode(coinValueList,change,knownResults):
	minCoins=change
	
	
def main():
	currentValue=13
	print(recMC([1,5,10,25],13))
