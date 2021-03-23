import sys
arr = {}

m = sys.stdin.readline().split(' ')
while m[0] != 0:
    if m[0] == '1':
        arr.update({m[1][:5]: 1})
    elif m[0] == '2':
        if m[1][:5] in arr:
            sys.stdout.write('1\n')
        else:
            sys.stdout.write('0\n')
    elif m[0] == '3':
        if m[1] in arr:
            del arr[m[1]]
    else:
        exit()
    m = sys.stdin.readline().split(' ')