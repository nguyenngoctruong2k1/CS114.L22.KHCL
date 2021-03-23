n = int(input())
arr = []

def ucln(a, b):
    if a % b == 0:
        return b
    return ucln(b, a % b)

for i in range(n):
    arr = list(map(int, input().split()))
    
    uc = ucln(arr[0], arr[1])
    arr[0] //= uc
    arr[1] //= uc
    
    if arr[1] > 1:
        print (arr[0], arr[1])
    else:
        print (arr[0])

#test 7 > 60