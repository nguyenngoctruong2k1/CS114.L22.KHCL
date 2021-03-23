import math
arr = list(map(int,input().split()))

n = arr[0]
m = arr[1]
a = arr[2]

print(math.ceil(n / a) * math.ceil(m / a))