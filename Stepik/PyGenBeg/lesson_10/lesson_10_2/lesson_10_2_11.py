s = input()

i1 = s.find('h')
i2 = s.rfind('h')

print(s[:i1] + s[i1:i2 + 1:-1] + s[i2:])
