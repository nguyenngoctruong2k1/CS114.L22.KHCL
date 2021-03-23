import math

a = float(input())
b = float(input())
c = float(input())
if a + b > c and a + c > b and b + c > a:
    p = (a + b + c) / 2
    s = round(math.sqrt(p * (p - a) * (p - b) * (p - c)), 2)
    
    if a == b == c: 
        print('Tam giac deu', end=', ') 
    elif a == b or a == c or b ==c:
        print('Tam giac can', end=', ')
    elif a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b:
        print('Tam giac vuong', end=', ')
    else:
        print('Tam giac thuong', end=', ')
        
    print('dien tich = {0:g}'.format(s))
else:
    print('Khong phai tam giac')