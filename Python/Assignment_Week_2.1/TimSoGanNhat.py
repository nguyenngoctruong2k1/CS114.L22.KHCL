n = int(input())
str = list(map(int,input().split()))
str1 = list(map(int,input().split()))
k = str1[0]
x = str1[1]

def TimKiem(x, lst, l, r):
    m = l + (r - l) * (x - lst[l]) // (lst[r] - lst[l])
    if lst[l] >= x:
        return l
    if lst[r] <= x:
        return r
    if x < lst[m]:
        return TimKiem(x, lst, l, m)
    if m + 1 <= n and x > lst[m + 1]:
        return TimKiem(x, lst, m+1, r)
    return m

if x < str[0]:
    l = 0
    r = k
elif x > str[-1]:
    r = n
    l = n - k
else:
    l = TimKiem(x, str, 0, n - 1)
    r = l + 1
    for i in range(k):
        if l < 0:
            r += 1
        elif r > n:
            l -= 1
        elif x - str[l] > str[r] - x:
            r += 1
        else:
            l -= 1
    l += 1
while l <= r - 1:
    print(str[l], end =' ')
    l += 1