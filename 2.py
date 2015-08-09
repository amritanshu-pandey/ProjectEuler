T = int(input())
while T>0:
	N = int(input())
	a = 1
	b = 2
	y = 0
	l = [2]
	while b<N:
		y=b
		b=a+b
		if b>N:
			break
		a = y
		if b%2==0:
			l.append(b)
	print(sum(l))
	T = T-1
