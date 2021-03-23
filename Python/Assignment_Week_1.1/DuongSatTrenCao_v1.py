input = input()

k = int(input.split()[0])
t = int(input.split()[1])

if (t // k) % 2 == 0:
    print(t % k) 
else:
    print(k - t % k)