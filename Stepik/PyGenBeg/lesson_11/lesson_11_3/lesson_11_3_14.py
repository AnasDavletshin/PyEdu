strs = []
for _ in range(int(input())):
    strs.append(input())

symbols = []
for s in strs:
    symbols.extend(s)

print(symbols)
