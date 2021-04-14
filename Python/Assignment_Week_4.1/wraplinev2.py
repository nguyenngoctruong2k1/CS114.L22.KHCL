import sys
fo = open("D:\input.txt", "r")
str = fo.readline()
n = int(fo.read())
fo.close()
# str = input()
# n = int(sys.stdin.readline())
lst = []
#lst: Danh sách những vị trí có thể ngắt

lst.append(0)
while True:
    # k: vị trí của dấu cách kế tiếp
    k = str.find(' ', lst[-1])
    if k == -1:
        lst.append(len(str))
        break
    if lst[-1] == k:
        lst[-1]=k+1
    else:
        lst.append(k+1)
i = 2
try:
    while True:
        if lst[i]-lst[i-2] <= n:
            lst.pop(i-1)
        else:
            i += 1
except:
    False
fo = open("D:\output.txt", "w+")
for i in range(len(lst)-1):
    #print(str[lst[i]:lst[i+1]])
    fo.write(str[lst[i]:lst[i+1]]+'\n')
fo.close()


