import sys
arr = {}
m = sys.stdin.readline().split()
result = ""
while m[0] != '0':
    if m[0] == '1':
        arr.update({m[1]:1})
    elif m[1] in arr:
        result += "1\n"
    else:
        result += "0\n"
    m = sys.stdin.readline().split()
print(result)