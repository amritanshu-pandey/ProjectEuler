
T = int(input())

BASE_NUM = {
0: '',
1 : 'One ',
2 : 'Two ',
3 : 'Three ',
4 : 'Four ',
5 : 'Five ',
6 : 'Six ',
7 : 'Seven ',
8 : 'Eight ',
9 : 'Nine '
	}
	
TENS_LIST = {
0: '',
1: 'Ten ',
2: 'Twenty ',
3: 'Thirty ',
4: 'Forty ',
5: 'Fifty ',
6: 'Sixty ',
7: 'Seventy ',
8: 'Eighty ',
9: 'Ninety '	
	}
	
TEEN_LIST = {
0: 'Ten ',
1: 'Eleven ',
2: 'Twelve ',
3: 'Thirteen ',
4: 'Fourteen ',
5: 'Fifteen ',
6: 'Sixteen ',
7: 'Seventeen ',
8: 'Eighteen ',
9: 'Nineteen '
}

BASE_FIG = {
'T': 'Thousand ',
'M': 'Million ',
'B': 'Billion ',
'Tr': 'Trillion '
	}
	
	
def num_to_word(inp_list):
	rev_inp_list = inp_list[::-1]
	#print('Reversed input: ',rev_inp_list)
	if len(rev_inp_list)==1:
		rev_inp_list.append(0)
		rev_inp_list.append(0)
	elif len(rev_inp_list)==2:
		rev_inp_list.append(0)
	elif len(rev_inp_list)==4:
		rev_inp_list.append(0)	
		rev_inp_list.append(0)
	elif len(rev_inp_list)==5:
		rev_inp_list.append(0)	
	elif len(rev_inp_list)==7:
		rev_inp_list.append(0)	
		rev_inp_list.append(0)
	elif len(rev_inp_list)==8:
		rev_inp_list.append(0)
	elif len(rev_inp_list)==10:
		rev_inp_list.append(0)	
		rev_inp_list.append(0)
	elif len(rev_inp_list)==11:
		rev_inp_list.append(0)
	elif len(rev_inp_list)==13:
		rev_inp_list.append(0)	
		rev_inp_list.append(0)
	elif len(rev_inp_list)==14:
		rev_inp_list.append(0)
	ones = rev_inp_list[0]
	tens = rev_inp_list[1]
	hundreds = rev_inp_list[0:3][::-1]
	thousands = rev_inp_list[3:6][::-1]
	if thousands==[0,0,0]:
		th_sep=chr(00)
	else:
		th_sep=BASE_FIG['T']
	millions = rev_inp_list[6:9][::-1]
	if millions==[0,0,0]:
		mi_sep=chr(00)
	else:
		mi_sep=BASE_FIG['M']
	billions = rev_inp_list[9:12][::-1]
	if billions==[0,0,0]:
		bi_sep=chr(00)
	else:
		bi_sep=BASE_FIG['B']
	trillions = rev_inp_list[12:][::-1]
	if trillions==[0,0,0]:
		tr_sep=chr(00)
	else:
		tr_sep=BASE_FIG['Tr']
	#print('Ones : ',ones)
	#print('Tens : ',tens)
	##print('Hundreds : ',hundreds)
	#print('Thousands : ',thousands)
	#print('Millions : ',millions)
	#print('Billions : ',billions)
	if len(rev_inp_list)<=3:
		if(hundreds==[0,0,0]):
			print('Zero')
		else:
			print(hundred_to_words(hundreds))
	elif len(rev_inp_list)<=6:
		print(hundred_to_words(thousands)+th_sep+hundred_to_words(hundreds))
	elif len(rev_inp_list)<=9:
		print(hundred_to_words(millions)+mi_sep+hundred_to_words(thousands)+th_sep+hundred_to_words(hundreds))
	elif len(rev_inp_list)<=12:
		print(hundred_to_words(billions)+bi_sep+hundred_to_words(millions)+mi_sep+hundred_to_words(thousands)+th_sep+hundred_to_words(hundreds))
	elif len(rev_inp_list)<=15:
		print(hundred_to_words(trillions)+tr_sep+hundred_to_words(billions)+bi_sep+hundred_to_words(millions)+mi_sep+hundred_to_words(thousands)+th_sep+hundred_to_words(hundreds))
def hundred_to_words(hun_list):
	rev_hun_list = hun_list[::-1]
	ones = rev_hun_list[0]
	tens = rev_hun_list[1]
	hundreds = rev_hun_list[2]
	if hundreds == 0:
		if tens==1:
			hundred_out = TEEN_LIST[ones] 
			#print(hundred_out)
		else:
			hundred_out = TENS_LIST[tens]+BASE_NUM[ones]
			#print(hundred_out)
	elif tens==1:
		hundred_out = BASE_NUM[hundreds]+'Hundred '+TEEN_LIST[ones] 
		#print(hundred_out)
	else:
		hundred_out = BASE_NUM[hundreds]+'Hundred '+TENS_LIST[tens]+BASE_NUM[ones]
		#print(hundred_out)
	return hundred_out
	
		
	
while T>0:
	for i in range(0,100000000):
		N = str(i)
		len_n = len(N)
		N_LIST = [int(i) for i in list(N)]
		N = int(N)
		#print('Input Number: ', N)
		#print('Listified input: ',N_LIST) 
		#print('Length: ',len_n)
		num_to_word(N_LIST)
	T=T-1
