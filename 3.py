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
	if isPrime(N):
		print(N)
	else:
		l = []
		for i in range(2,int((N)/2)+1):
			if N%i==0:
				div = int(N/i)
				if isPrime(div):
					#l.append(int(N/i))
					print(div)
					break
	T=T-1
