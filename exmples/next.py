def getNext(pattern):
	i = 0
	nextArray = [0] * len(pattern) 
	nextArray[0] = -1
	j = -1
	while(i < len(pattern)):
		if(j == -1 or pattern[i] == pattern[j]):
			++i
			++j
			nextArray[i] = j
		else:
			j = nextArray[j]
	return nextArray			

print getNext('abaabcac')
