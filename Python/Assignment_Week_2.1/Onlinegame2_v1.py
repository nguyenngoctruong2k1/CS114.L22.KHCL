import sys
arr = {}
result = ""
while True:
    info = sys.stdin.readline().split()
    try:
        m = list(map(int,info))
    except ValueError:
        if info[0] == '1':
            arr[info[1]] = True
        elif info[0] == '2':
            if info[1] in arr:
                sys.stdout.write('1\n')
            else:
                sys.stdout.write('0\n')
        elif info[0] == '3':
            if info[1] in arr:
                del arr[info[1]]
        else:
            exit()
        continue
    if m[0] == 0:
        break
    elif m[0] == 1:
        arr[m[1]] = True
    elif m[0] == 2:
        if m[1] in arr:
            print("1")
        else:
            print("0")
    elif m[0] == 3:
        if m[1] in arr:
            del arr[m[1]]
        else:
            pass
    else:
        break