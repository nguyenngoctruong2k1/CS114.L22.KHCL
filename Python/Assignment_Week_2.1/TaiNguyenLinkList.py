import sys
m, n = map(int, sys.stdin.readline().split(' '))
a = []

for i in range(m):
    a.append([int(j) for j in sys.stdin.readline().split(' ')])

posit = list(map(int, sys.stdin.readline().split(' ')))

for i in range(m):
    for j in range(n):
        if (i < posit[1] and i < posit[3]) or (i > posit[1] and i > posit[3]):
            a[i][j] = 0
        else:
            if (j < posit[0] and j < posit[2]) or (j > posit[0] and j > posit[2]):
                a[i][j] = 0

for i in range(m):
        for j in range(n):
            print("%3d " % a[i][j], end='')
        print()