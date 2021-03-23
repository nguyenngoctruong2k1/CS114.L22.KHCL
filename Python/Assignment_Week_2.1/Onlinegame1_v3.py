import sys
arr = {}
result = ""
m = sys.stdin.readline().split()
while m[0] != '0':
    if len(m) == 0:
        exit()

    if m[0] == '1':
        arr.update({m[1]:1})
    elif m[0] == '2':
        if m[1] in arr:
            result += "1\n"
            
        else:
            result += "0\n"
            arr.update({m[1]:0})
    else:
        if m[1] in arr:
            arr.update({m[1]:0})
    m = sys.stdin.readline().split()
print(result)