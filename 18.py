T = int(input())
while T>0:
	N= int(input())
	d = 0
	tri = []
	slist = []
	while d<N:
		tri.append([int(i) for i in input().split()])
		d=d+1
	#for i in range(0,N):
		#print(tri[i])
	tri_new = [list(i) for i in tri]
	for i in range(0,N-1):
		lists = [list(tri[i+1]) for p in range(0,i+1)]
#		print('lists: ',lists)
		for k in range(0,i+1):
			#orig1 = tri[i+1][k]
			#orig2 = tri[i+1][k+1]
			new1=tri[i+1][k] + tri_new[i][k]
			new2=tri[i+1][k+1] + tri_new[i][k]
			lists[k][k]=new1
			lists[k][k+1]=new2
			#if(new1>orig1):
			#	tri_new[i+1][k]=new1
			#if(new2>orig2):
			#	tri_new[i+1][k+1]=new2
#		print('New lists: ',lists)
		fin = [0 for a in range(0,i+2)]
#		print('orig_fin: ',fin)
		if len(lists)==1:
			fin = list(lists[0])
		else:
#			print('g: ',i+1,' h: ',i+2)
			for g in range(0,i):
				for h in range(0,i+2):
					if lists[g][h]>lists[g+1][h]:
						fin[h]=lists[g][h]
					else:
						fin[h]=lists[g+1][h]
#		print('Fin: ',fin)
		for l in range(0,len(fin)):
			tri_new[i+1][l]=fin[l]
#	for i in range(0,N):
#		print(tri_new[i])
	print(max(tri_new[N-1]))
	T=T-1
