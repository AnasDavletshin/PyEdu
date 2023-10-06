s = input()

total = 0
for ch in s:
    if ch != ch.upper():
        total += 1
print(total)
