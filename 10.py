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
	s = 0
	l=[]
	for i in range(2,N+1):
		if isPrime(i):
			#print(i)
			l.append(i)
	print(sum(l))
	T=T-1
