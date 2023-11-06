strs = []

for i in range(ord('a'), ord('z') + 1):
    strs.append(chr(i) * (i - ord('a') + 1))

print(strs)
