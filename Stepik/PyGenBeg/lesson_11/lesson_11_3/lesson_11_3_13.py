strs = []
for _ in range(int(input())):
    strs.append(input())

k = int(input())

for s in strs:
    if len(s) >= k:
        print(s[k - 1], end='')
