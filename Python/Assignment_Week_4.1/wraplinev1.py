import sys
str = input()
n = int(sys.stdin.readline())
lst = []

lst.append(0)
lst.append(str.find(' ') + 1)
while lst[-1] != len(str):
    k = str.find(' ', lst[-1]) + 1
    if k == 0:
        k = len(str)
    if k - lst[-2]<=n:
        lst.pop()
    lst.append(k)

for i in range(len(lst)-1):
    print(str[lst[i]:lst[i+1]])