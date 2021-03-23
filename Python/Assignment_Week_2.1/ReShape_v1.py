m, n = list(map(int, input().split()))
r, c = list(map(int, input().split()))

s = []
flag = m * n != r * c
for i in range(m):
    matrix = input().split()
    if flag:
        print(' '.join(matrix))
    else:
        s = s + matrix

arr = []

if m * n == r * c:
    for i in range(r):
        arr.append(' '.join(s[i * c : (i + 1) * c]))

print('\n'.join(arr))