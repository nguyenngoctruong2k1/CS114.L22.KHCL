n = int(input())
str = []

def average(s):
    t = 0
    for i in s:
        t = t + i
    if t % len(s) == 0:
        return t // len(s)
    else:
        return t // len(s) + 1

for i in range(n):
    k = int(input())
    m = input()
    str.append(list(map(int, m.split())))
    print(average(str[i]))


