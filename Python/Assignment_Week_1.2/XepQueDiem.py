import math
n = int(input())

for i in range(n):
    x = int(input())
    c = math.ceil(x/2)
    if c < 2:
        c = 2
    print(2 * c - x)