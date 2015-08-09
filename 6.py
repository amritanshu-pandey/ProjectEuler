from math import pow
T = int(input())
while T>0:
	N = int(input())
	sumn = (N*(N+1))>>1
	sumn2 = sumn*sumn
	sum2n = int(N*(N+1)*(2*N+1)/6)
	print(sumn2-sum2n)
	T=T-1
