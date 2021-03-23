s1 = input()
s2 = input()

if len(s1) != len(s2):
    print('NO')
else:
    for i in range(len(s1)):
        if s1[i] != s2[- (i + 1)]:
            print('NO')
            exit()
    print('YES')