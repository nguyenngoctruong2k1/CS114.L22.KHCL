const = ['lios', 'liala', 'etr', 'etra', 'initis', 'inites']

def LoaiTu(x):
    for i in const:
        if len(x) >= len(i) and x.find(i) == len(x) - len(i):
            return const.index(i)
    return -1

str = input().split()

lst = list(map(LoaiTu,str))

if -1 in lst:
    print('NO')
elif len(lst) == 1:
    print('YES')
else:
    dt = 3
    if dt not in lst:
        dt = 2
    if lst.count(dt) != 1:
        print('NO')
        exit()
    for x in lst:
        if x % 2 != dt % 2:
            print('NO')
            exit()
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            print('NO')
            exit()
    print('YES')

