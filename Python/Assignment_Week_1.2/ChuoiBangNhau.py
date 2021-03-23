n = int(input())

for i in range(n):
    s1 = input()
    s2 = input()
    flag = False
    if len(s1) == len(s2):
        for x in s1:
            if s2.find(x) >= 0:
                flag = True
                break
    if flag:
        print('YES')
    else:
        print('NO')