m, n = list(map(int, input().split()))
r, c = list(map(int, input().split()))

matrix = []
for i in range(m):
    matrix.append(input())
    if m * n != r * c:
        print(matrix[i])
        
if m * n == r * c:
    s = ' '.join(matrix).split()
    for i in range(r):
        print(' '.join(s[i * c : (i + 1) * c]))