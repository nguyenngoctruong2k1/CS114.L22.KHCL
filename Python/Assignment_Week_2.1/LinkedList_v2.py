import sys
lst = []

Info = sys.stdin.readline().split()
while Info[0] != "6":
    if Info[0] == "0":
        lst.insert(0,Info[1])
    elif Info[0] == "1":
        lst.append(Info[1])
    elif Info[0] == "2":
        if Info[1] in lst:
            lst.insert(lst.index(Info[1]) + 1, Info[2])
        else:
            lst.insert(0,Info[2])
    elif Info[0] == "3":
        if Info[1] in lst:
            lst.remove(Info[1])
    elif Info[0] == "4":
        while Info[1] in lst:
            lst.remove(Info[1])
    elif Info[0] == "5":
        if len(lst) > 0:
            lst.pop(0)
    Info = sys.stdin.readline().split()

if len(lst) != 0:
    print(' '.join(lst))
else:
    print('blank')