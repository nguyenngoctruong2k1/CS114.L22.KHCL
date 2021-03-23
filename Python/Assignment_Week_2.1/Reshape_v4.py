m, n = list(map(int, input().split()))
r, c = list(map(int, input().split()))

matrix = []
s = []
for i in range(m):
    matrix = input()
    if m * n != r * c:
        print(matrix)
    else:
        s += matrix.split()
        while len(s) >= c:
            print(' '.join(s[:c]))
            s = s[c:]