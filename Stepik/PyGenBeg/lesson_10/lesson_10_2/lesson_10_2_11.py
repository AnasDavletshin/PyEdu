s = input()

i1 = s.find('h')
i2 = s.rfind('h')

print(s[:i1 + 1], s[i2-1:i1:-1], s[i2:], sep='')
