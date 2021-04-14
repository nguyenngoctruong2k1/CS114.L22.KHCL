import sys
n = int(sys.stdin.readline())
arr = []
maybom = []
for i in range(n):
    arr.append(sys.stdin.readline())
# xây dựng dữ liệu đường ống
#       0
#     *****
#   3 *   * 1
#     *****
#       2
Ong = {
    '1':(0,2),
    '2':(1,3),
    '3':(1,2),
    '4':(2,3),
    '5':(0,3),
    '6':(0,1),
    '7':(0,2,1,3)
}

def output(s,k): 
    # s : loại ống
    # k : đầu vào
    # (return đầu ra) -> return đầu vào của ô tiếp theo
    try:
        m = Ong[s][Ong[s].index(k) - 1]
        if Ong[s].index(k) % 2 == 0:
            m = Ong[s][Ong[s].index(k) + 1]
        if m<2:
            return m+2
        else:
            return m-2    
    except:
        return -1

for i in range(n):
    for j in range(len(arr[i])):
        # lấy tọa độ của các máy bơm
        if 'a'<=arr[i][j]<='z':
            maybom.append((i,j))

def XuLyO(a,i,j,k,s):
    # a: máy bơm,
    # i,j: tọa độ,
    # k: hướng nước vào
    # s: lưu tọa độ, s[-1]: lưu cờ báo tràn
    # Lấy Giá trị của ô trước đó - để kiểm tra xem nó có phải là máy bơm không
    Last = ''
    if k == 0:
        Last = arr[i-1][j]
    elif k == 1:
        Last = arr[i][j+1]
    elif k == 2:
        Last = arr[i+1][j]
    else:
        Last = arr[i][j-1]
    # Khi máy bơm ở biên
    if i>=n or i<0 or j<0 or j>len(arr[0]):
        if Last==a:
            s.append(False)
        else:
            s.append(True)
        return
    # Khi ô hiện tại đang xét là bể chứa
    if arr[i][j] == a.upper():
        s.append(False)
        return
        # Lấy giá trị đầu ra của ống nước ở ô hiện tại, đồng thời kiểm tra ống nước có khớp không
    k = output(arr[i][j],k)
    # Khi ống nước của ô hiện tại không khớp với phần trước nó
    if k == -1:
        if Last == a:
            s.append(False)
        else:
            s.append(True)
        return
    s.append((i,j))
    # Đệ quy - xét đến ô đầu ra của ống nước ở ô hiện tại
    if k == 0:
        XuLyO(a,i+1,j,k,s)
    elif k == 1:
        XuLyO(a,i,j-1,k,s)
    elif k == 2:
        XuLyO(a,i-1,j,k,s)
    else:
        XuLyO(a,i,j+1,k,s)

def XuLyMayBom(x):
    global s
    i,j = x
    # 1 máy bơm sẽ có 4 con đường đi =  4 mảng để lưu tọa độ của con đường đang đi, phần tử tử cuối chứa flag
    s1 = []
    XuLyO(arr[i][j],i+1,j,0,s1)
    s2 = []
    XuLyO(arr[i][j],i-1,j,2,s2)
    s3 = []
    XuLyO(arr[i][j],i,j+1,3,s3)
    s4 = []
    XuLyO(arr[i][j],i,j-1,1,s4)
    s += [s1,s2,s3,s4]
def Count():
    first_leak = list(map(lambda x: len(x), filter(lambda x: x[-1], s)))

    first_leak = 0 if len(first_leak) == 0 else min(first_leak) - 1
    
# lưu các tọa độ trong trong 1 tập hợp để loại bỏ những ô giống nhau
TOADO = set()
flag = 1
# s: lưu các con đường để đi
s = []
for x in maybom:
    XuLyMayBom(x)
# Ban đầu TimeLength lưu list các độ dài của đường đi bị rò rỉ nước
TimeLength = list(map(lambda x: len(x), filter(lambda x: x[-1], s)))
# Lúc sau lưu giá trị nhỏ nhất của đường đi bị rò rỉ nước
TimeLength = 0 if len(TimeLength) == 0 else min(TimeLength) - 1

for x in s:
    # Xác định chỉ số k, độ dài lớn nhất mà nó có đi chảy trước khi có chỗ rò rỉ nước
    k = min(TimeLength, len(x)-1) if TimeLength else len(x)-1
    TOADO = TOADO.union(x[:k])
flag = 1 if TimeLength == 0 else -1
print(len(TOADO)*flag)