n = int(input())
i = 2
s = 1

while i <= n//2:
    if n % i == 0:
        s += i
    i += 1

print(s)
