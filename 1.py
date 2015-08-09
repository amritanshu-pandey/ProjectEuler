from math import *
T = int(input())
while T>0:
	N = int(input())
	no3=0
	
	no3 = ((N-1)//3)
	sum3 = ((no3)*(2*3+(no3-1)*3))>>1
	no5 = ((N-1)//5)
	sum5 = ((no5)*(2*5+(no5-1)*5))>>1
	no15 = ((N-1)//15)
	sum15 = ((no15)*(2*15+(no15-1)*15))>>1
	print(int(sum3+sum5-sum15))
	T = T-1	
