str = input()

# 0: Nam --- 1: Nu --- -1: kophai
def tinhtu(str):
	if str.find('lios') > -1 and str.find('lios') - len(str) == -4:
		return 0
	elif str.find('liala') > -1 and str.find('liala') - len(str) == -5:
		return 1
	else:
		return -1
	

def danhtu(str):
	if str.find('etr') - len(str) == -3:
		return 0
	elif str.find('etra') - len(str) == -4:
		return 1
	else:
		return -1

def dongtu(str):
	if str.find('initis') - len(str) == -6:
		return 0
	elif str.find('inites') - len(str) == -6:
		return 1
	else:
		return -1

def tu(arr):
	if tinhtu(arr) >=0:
		return 0 + tinhtu(arr)
	elif danhtu(arr) >=0:
		return 2 + danhtu(arr)
	elif dongtu(arr) >=0:
		return 4 + dongtu(arr)
	else:
		return -1

def menhde(arr):
	pre = -1
	dt = False
	for i in arr:
		if tu(i) == -1:
			return False
		if pre > -1:
			if (pre - tu(i)) % 2 == 1:
				return False
			if pre > tu(i):
				return False 
			
		if tu(i) // 2 == 1:
				if dt:
					return False
				else:
					dt = True
		pre = tu(i)
	if not dt:
		return dt
	return True

arr = str.split()

if (len(arr) == 1 and tu(arr[0]) >= 0) or menhde(arr):
	print('YES')
else:
	print('NO')