import sys

rubik = []
color = sys.stdin.readline().split()
for i in color:
    k = []
    for j in range(9):
        k.append(i)
    rubik.append(k)
str = sys.stdin.readline().split()
str.reverse()
sys.stdin.readline()

def Xoay120(a, b, c):
    return b, c, a
def Xoay_120(a, b, c):
    return c, a, b

# Xoay U
def move_U1_():
    rubik[0][0], rubik[2][4],rubik[3][8] = Xoay120(rubik[0][0], rubik[2][4],rubik[3][8])
def move_U1():
    rubik[0][0], rubik[2][4],rubik[3][8] = Xoay_120(rubik[0][0], rubik[2][4],rubik[3][8])
def move_U2_():
    rubik[0][0], rubik[2][4],rubik[3][8] = Xoay120(rubik[0][0], rubik[2][4],rubik[3][8])
    rubik[0][1], rubik[2][6],rubik[3][3] = Xoay120(rubik[0][1], rubik[2][6],rubik[3][3])
    rubik[0][2], rubik[2][5],rubik[3][7] = Xoay120(rubik[0][2], rubik[2][5],rubik[3][7])
    rubik[0][3], rubik[2][1],rubik[3][6] = Xoay120(rubik[0][3], rubik[2][1],rubik[3][6])
def move_U2():
    rubik[0][0], rubik[2][4],rubik[3][8] = Xoay_120(rubik[0][0], rubik[2][4],rubik[3][8])
    rubik[0][1], rubik[2][6],rubik[3][3] = Xoay_120(rubik[0][1], rubik[2][6],rubik[3][3])
    rubik[0][2], rubik[2][5],rubik[3][7] = Xoay_120(rubik[0][2], rubik[2][5],rubik[3][7])
    rubik[0][3], rubik[2][1],rubik[3][6] = Xoay_120(rubik[0][3], rubik[2][1],rubik[3][6])
# Xoay R
def move_R1_():
    rubik[0][8], rubik[3][0],rubik[1][4] = Xoay120(rubik[0][8], rubik[3][0],rubik[1][4])
def move_R1():
    rubik[0][8], rubik[3][0],rubik[1][4] = Xoay_120(rubik[0][8], rubik[3][0],rubik[1][4])
def move_R2_():
    rubik[0][8], rubik[3][0],rubik[1][4] = Xoay120(rubik[0][8], rubik[3][0],rubik[1][4])
    rubik[0][3], rubik[3][1],rubik[1][6] = Xoay120(rubik[0][3], rubik[3][1],rubik[1][6])
    rubik[0][7], rubik[3][2],rubik[1][5] = Xoay120(rubik[0][7], rubik[3][2],rubik[1][5])
    rubik[0][6], rubik[3][3],rubik[1][1] = Xoay120(rubik[0][6], rubik[3][3],rubik[1][1])
def move_R2():
    rubik[0][8], rubik[3][0],rubik[1][4] = Xoay_120(rubik[0][8], rubik[3][0],rubik[1][4])
    rubik[0][3], rubik[3][1],rubik[1][6] = Xoay_120(rubik[0][3], rubik[3][1],rubik[1][6])
    rubik[0][7], rubik[3][2],rubik[1][5] = Xoay_120(rubik[0][7], rubik[3][2],rubik[1][5])
    rubik[0][6], rubik[3][3],rubik[1][1] = Xoay_120(rubik[0][6], rubik[3][3],rubik[1][1])

# Xoay L
def move_L1_():
    rubik[0][4], rubik[1][8],rubik[2][0] = Xoay120(rubik[0][4], rubik[1][8],rubik[2][0])
def move_L1():
    rubik[0][4], rubik[1][8],rubik[2][0] = Xoay_120(rubik[0][4], rubik[1][8],rubik[2][0])
def move_L2_():
    rubik[0][4], rubik[1][8],rubik[2][0] = Xoay120(rubik[0][4], rubik[1][8],rubik[2][0])
    rubik[0][1], rubik[1][6],rubik[2][3] = Xoay120(rubik[0][1], rubik[1][6],rubik[2][3])
    rubik[0][5], rubik[1][7],rubik[2][2] = Xoay120(rubik[0][5], rubik[1][7],rubik[2][2])
    rubik[0][6], rubik[1][3],rubik[2][1] = Xoay120(rubik[0][6], rubik[1][3],rubik[2][1])
def move_L2():
    rubik[0][4], rubik[1][8],rubik[2][0] = Xoay_120(rubik[0][4], rubik[1][8],rubik[2][0])
    rubik[0][1], rubik[1][6],rubik[2][3] = Xoay_120(rubik[0][1], rubik[1][6],rubik[2][3])
    rubik[0][5], rubik[1][7],rubik[2][2] = Xoay_120(rubik[0][5], rubik[1][7],rubik[2][2])
    rubik[0][6], rubik[1][3],rubik[2][1] = Xoay_120(rubik[0][6], rubik[1][3],rubik[2][1])

# Xoay B
def move_B1_():
    rubik[2][8], rubik[1][0],rubik[3][4] = Xoay120(rubik[2][8], rubik[1][0],rubik[3][4])
def move_B1():
    rubik[2][8], rubik[1][0],rubik[3][4] = Xoay_120(rubik[2][8], rubik[1][0],rubik[3][4])
def move_B2_():
    rubik[2][8], rubik[1][0],rubik[3][4] = Xoay120(rubik[2][8], rubik[1][0],rubik[3][4])
    rubik[2][3], rubik[1][1],rubik[3][6] = Xoay120(rubik[2][3], rubik[1][1],rubik[3][6])
    rubik[2][7], rubik[1][2],rubik[3][5] = Xoay120(rubik[2][7], rubik[1][2],rubik[3][5])
    rubik[2][6], rubik[1][3],rubik[3][1] = Xoay120(rubik[2][6], rubik[1][3],rubik[3][1])
def move_B2():
    rubik[2][8], rubik[1][0],rubik[3][4] = Xoay_120(rubik[2][8], rubik[1][0],rubik[3][4])
    rubik[2][3], rubik[1][1],rubik[3][6] = Xoay_120(rubik[2][3], rubik[1][1],rubik[3][6])
    rubik[2][7], rubik[1][2],rubik[3][5] = Xoay_120(rubik[2][7], rubik[1][2],rubik[3][5])
    rubik[2][6], rubik[1][3],rubik[3][1] = Xoay_120(rubik[2][6], rubik[1][3],rubik[3][1])

for x in str:
    if x == "U":
        move_U1()
    elif x == "U'":
        move_U1_()
    elif x == "u":
        move_U2()
    elif x == "u'":
        move_U2_()
    # end U
    elif x == "R":
        move_R1()
    elif x == "R'":
        move_R1_()
    elif x == "r":
        move_R2()
    elif x == "r'":
        move_R2_()
    # end R
    elif x == "B":
        move_B1()
    elif x == "B'":
        move_B1_()
    elif x == "b":
        move_B2()
    elif x == "b'":
        move_B2_()
    # end B
    elif x == "L":
        move_L1()
    elif x == "L'":
        move_L1_()
    elif x == "l":
        move_L2()
    elif x == "l'":
        move_L2_()
    # end R

for x in rubik:
    print(*x)