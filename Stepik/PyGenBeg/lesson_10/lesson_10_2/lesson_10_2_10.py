s = input()
i1 = s.find('f')
if i1 == -1:
    print(-2)
else:
    i2 = s[i1 + 1:].find('f')
    if i2 == -1:
        print(-1)
    else:
        print(i2 + i1 + 1)
