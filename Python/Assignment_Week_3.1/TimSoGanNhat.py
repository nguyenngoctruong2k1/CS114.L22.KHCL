import bisect
n = int(input())
str = list(map(int,input().split()))
while True:
    s = input()
    if s =='':
        exit()
    k, x = list(map(int,s.split()))
    if x < str[0]:
        l = 0
        r = k
    elif x > str[-1]:
        r = n
        l = n - k
    else:
        l = bisect.bisect_left(str, x, 0, n-1)
        r = l + 1
        for i in range(k):
            if l < 0:
                r += 1
            elif r >= n:
                l -= 1
            elif x - str[l] > str[r] - x:
                r += 1
            else:
                l -= 1
        l += 1
    print(str[l], str[r-1])