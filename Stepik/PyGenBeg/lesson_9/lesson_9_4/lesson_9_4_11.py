s = input()

total = 0
for d in range(10):
    total += s.count(str(d))
print(total)
