k = input()
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i = 0
j = 0
while i < len(a) or j < len(b):
    if i == len(a):
        print(b[j], end = ' ')
        j += 1
    elif j == len(b):
        print(a[i], end = ' ')
        i += 1
    elif a[i] > b[j]:
        print(b[j], end = ' ')
        j += 1
    else:
        print(a[i], end = ' ')
        i += 1