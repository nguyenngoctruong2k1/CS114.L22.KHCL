str = input()

str = str.lower()

s = ''
for i in str:
	if i not in 'aoyeui':
		s = s + '.' + i

print(s)