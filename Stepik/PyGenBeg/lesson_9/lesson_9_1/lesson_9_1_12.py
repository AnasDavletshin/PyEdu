s = input()

totalP = totalZ = 0
for c in s:
    if c == '+':
        totalP += 1
    elif c == '*':
        totalZ += 1

print('Символ + встречается ' + str(totalP) + ' раз')
print('Символ * встречается ' + str(totalZ) + ' раз')
