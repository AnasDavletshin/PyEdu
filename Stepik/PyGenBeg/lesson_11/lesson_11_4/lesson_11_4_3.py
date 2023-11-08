n = int(input())

xlist = []
for i in range(n):
    xlist.append(int(input()))

print(*xlist, sep='\n')
print()
for x in xlist:
    print(x**2 + 2 * x + 1, end='\n')
