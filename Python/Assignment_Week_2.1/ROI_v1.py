h, w = list(map(int, input().split()))
photos = []
for i in range(h):
    photos.append(input().split())
top, left, bottom, right = list(map(int, input().split()))

for i in list(range(bottom + 1, h)) + list(range(0, top)):
    for j in range(w):
        photos[i][j] = '0'

for i in list(range(0, left)) + list(range(right + 1, w)):
    for j in range(top, bottom + 1):
        photos[j][i] = '0'

for i in photos:
    print(' '.join(i))