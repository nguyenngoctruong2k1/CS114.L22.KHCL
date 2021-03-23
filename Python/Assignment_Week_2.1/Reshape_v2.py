import numpy 

m, n = list(map(int, input().split()))
r, c = list(map(int, input().split()))

def _print(arr):
    for r in arr:
        for c in r:
            print(c, end=' ')
        print()

matrix = numpy.full((m,n), 0)
for i in range(m):
    matrix[i] = list(map(int, input().split()))

if m * n == r * c:
    _print(matrix.reshape(r,c))
else:
    _print(matrix)