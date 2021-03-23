h, w = list(map(int, input().split()))
photos = []
for i in range(h):
    photos.append(input())
top, left, bottom, right = list(map(int, input().split()))

_0 = photos[-1].replace('1', '0', photos[-1].count('1')) 

for i in range(h):
    if i not in range(top, bottom + 1):
        print(_0)
    else:
        print(_0[:left * 2], photos[i][left * 2: right * 2 + 1], _0[right * 2 + 1:], sep = '')