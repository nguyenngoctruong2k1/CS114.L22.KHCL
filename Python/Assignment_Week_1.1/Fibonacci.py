x = int(input())

if 1 <= x <= 30:
    fi = []
    fi.append(1)
    fi.append(1)
    if x <= 2:
        print(fi[x-1])
    else:
        i = 3
        while i <= x:
            fi.append(fi[-1] + fi[-2])
            i += 1
        print(fi[x-1])
else:
    print('So ', x, ' khong nam trong khoang [1,30].')