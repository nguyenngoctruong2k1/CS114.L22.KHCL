s = input()

k = 0
for i in range(len(s)):
	k = int(s[i]) ** len(s) + k

print(k == int(s))