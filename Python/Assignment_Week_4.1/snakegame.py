import sys
from collections import deque  
n, m ,c = list(map(int,sys.stdin.readline().split()))
arr = []
for i in range(n):
    arr.append(sys.stdin.readline())
str = sys.stdin.readline()
# đọc dữ liệu

snack = deque()
snack_head = ''
flag = []
for i in range(n):
    k = ['.'] * m
    flag.append(k)
# chuẩn bị

for i in range(len(arr)):
    k = arr[i].find('>') + arr[i].find('<') + arr[i].find('^') + arr[i].find('v') + 3
    if k != -1:
        snack.append((i,k))
        snack_head = arr[i][k]
        flag[i][k] = 'X'
        break
# lấy đầu của snack

def xacdinh(i,j):
    if 0 > i or n <= i or 0> j or m<=j:
        return
    if flag[i][j] == 'X' or arr[i][j] == '.':
        return
    snack.append((i, j))
    flag[i][j] = 'X'
    xacdinh(i+1,j)
    xacdinh(i-1,j)
    xacdinh(i,j+1)
    xacdinh(i,j-1)

if snack_head == '>':
    xacdinh(snack[0][0],snack[0][1]-1)
    xacdinh(snack[0][0]+1,snack[0][1])
    xacdinh(snack[0][0]-1,snack[0][1])
elif snack_head == '<':
    xacdinh(snack[0][0],snack[0][1]+1)
    xacdinh(snack[0][0]+1,snack[0][1])
    xacdinh(snack[0][0]-1,snack[0][1])
elif snack_head == '^':
    xacdinh(snack[0][0],snack[0][1]-1)
    xacdinh(snack[0][0],snack[0][1]+1)
    xacdinh(snack[0][0]+1,snack[0][1])
else:
    xacdinh(snack[0][0],snack[0][1]+1)
    xacdinh(snack[0][0],snack[0][1]-1)
    xacdinh(snack[0][0]-1,snack[0][1])

# kết thúc việc đọc tọa độ ban đầu của snack
def F1(i,j):
    global flag
    if 0 > i or n <= i or 0> j or m<=j:
        return True
    if flag[i][j] == 'X' and (i,j) != snack[-1]:
        return True
    
    snack.appendleft((i,j))

    k,l = snack.pop()
    flag[k][l] = '.'
    flag[i][j] = 'X'
    return False

def F():
    if snack_head == '<':
        return F1(snack[0][0],snack[0][1]-1)
    elif snack_head == '>':
        return F1(snack[0][0],snack[0][1]+1)
    elif snack_head == 'v':
        return F1(snack[0][0]+1,snack[0][1])
    else:
        return F1(snack[0][0]-1,snack[0][1])

def R():
    global snack_head
    if snack_head == '<':
        snack_head = '^'
    elif snack_head == '>':
        snack_head = 'v'
    elif snack_head == 'v':
        snack_head = '<'
    else:
        snack_head = '>'

def L():
    global snack_head
    if snack_head == '<':
        snack_head = 'v'
    elif snack_head == '>':
        snack_head = '^'
    elif snack_head == 'v':
        snack_head = '>'
    else:
        snack_head = '<'

for x in str:
    if x == 'R':
        R()
    elif x == 'L':
        L()
    elif x == 'F':
        if F():
            for x in flag:
                print(''.join(x))
            exit()


for i in range(len(snack)):
    flag[snack[i][0]][snack[i][1]] = '*'
flag[snack[0][0]][snack[0][1]] = snack_head
for x in flag:
    print(''.join(x))
# while True:
#     x = input()
#     if x == 'R':
#         R()
#     elif x == 'L':
#         L()
#     else:
#         if F():
#             break
#     for x in flag:
#         print(''.join(x))
#     print()