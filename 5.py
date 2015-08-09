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
	two = []
	x = 2
	while 2**x<N:
		two.append(2**x) 
		x=x+1
	three = []
	x = 2
	while 3**x<N:
		three.append(3**x) 
		x=x+1
	#two = [4,8,16,32]
	#three = [9,27] 
	print(two)
	print(three)
	l = []
	k = []
	F=N
	while F>0:
		  if isPrime(F):
			  l.append(F)
		  else:
			  k.append(F)
			  if F in two:
				  l.append(2)
			  elif F in three:
				  l.append(3)
		  F=F-1
	#print(l)
	#print(k)
	product = 1
	for x in l:
		product = product*x
	print(product)
	T=T-1
