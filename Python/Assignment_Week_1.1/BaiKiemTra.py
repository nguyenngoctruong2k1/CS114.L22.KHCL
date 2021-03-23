n = int(input())
k = int(input())
p = int(input())
q = int(input())

m = (p - 1) * 2 + q - 1
# m là vị trí của Alice tính từ 0 
if m - k >= 0:
	print((m - k)//2 + 1,(m - k) % 2 + 1)
elif m + k < n:
	print((m + k)//2 + 1,(m + k) % 2 + 1)
else:
	print(-1)