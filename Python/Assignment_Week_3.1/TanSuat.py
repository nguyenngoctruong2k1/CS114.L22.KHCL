q = int(input())
for i in range(q):
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    count = 0
    while k in arr:
        arr.remove(k)
        count +=1
    print(count)