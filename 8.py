T = int(input())
while T>0:
	INP = input().split()
	N = int(INP[0])
	K = int(INP[1])
	max_list = []
	num = str(input())
	#print('N: ',N,' K: ',K,' Num= ',num)
	for i in range(0,N-K+1):
		prod_list = num[i:i+K]
		#print(prod_list)
		prod = 1
		for i in prod_list:
			prod = prod*int(i)
		max_list.append(prod)
	#print('List: ',max_list)
	print(max(max_list))
	T = T-1
