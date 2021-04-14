import sys
str = input()
n = int(sys.stdin.readline())
lst = []

def Xuly(s):
    arr = [0]
    while True:
        k = s.find(' ',arr[-1]):
        if k != arr[-1]:
            arr.append(k)
        arr.append(k+1)
        if arr[-1] > n:
            break
    