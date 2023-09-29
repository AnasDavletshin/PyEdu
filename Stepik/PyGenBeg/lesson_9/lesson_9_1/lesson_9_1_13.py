s = input()

total = 0
for i in range(1, len(s)):
    if s[i - 1] == s[i]:
        total += 1

print(total)
