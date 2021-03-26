import math
r, c = list(map(int,input().split()))
arr = []
lenMax = []
for i in range(c):
    lenMax.append(0)
for i in range(r):
    arr.append(list(map(str,map(int,input().split()))))
    Len = list(map(len,arr[i]))
    lenMax = list(map(max,Len,lenMax)) 

def chuanhoa(s, n):
    return s.rjust(n)

for i in range(r):
    print(*list(map(chuanhoa,arr[i],lenMax)))


#test có 0011