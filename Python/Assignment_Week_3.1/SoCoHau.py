n, m = input().split()
if len(m) < len(n):
    print(0)
elif len(m) == len(n):
    if m >= n:
        print(1)
    else:
        print(0)
elif m[-len(n):] >= n:
    print(int(m[:len(m)-len(n)]) + 1)
else:
    print(int(m[:len(m)-len(n)]))