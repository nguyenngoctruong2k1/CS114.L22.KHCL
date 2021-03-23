f = float(input())

c = (f - 32) / 1.8
k = c + 273.15

print('{0:g}'.format(c), '{0:g}'.format(k))