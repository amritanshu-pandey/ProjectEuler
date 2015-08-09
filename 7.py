
T = int(input())
from math import sqrt

def isPrime(n):
	#print('inside F= ',n)
	for x in range(2,int(sqrt(n))+1):
		if n%x==0:
			return False
	return True

while T>0:
	N = int(input())
	count = 0
	l = []
	i=0
	while 1>0:
		i+=1
		if isPrime(i):
			l.append(i)
			count = count +1
			if(count > N):
				break
	print(l[-1])
	T=T-1
