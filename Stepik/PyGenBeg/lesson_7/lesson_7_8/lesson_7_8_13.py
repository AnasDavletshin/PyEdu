exitFlag = False
for a in range(1, 151):
    a5 = a ** 5
    for b in range(a, 151):
        b5 = b ** 5
        for c in range(b, 151):
            c5 = c ** 5
            for d in range(c, 151):
                s = a5 + b5 + c5 + d ** 5
                e = int(s ** 0.2)
                # print(a, b, c, d, e)
                if s == e ** 5:
                    print(a + b + c + d + e)
                    exitFlag = True
                    break
            if exitFlag:
                break
        if exitFlag:
            break
    if exitFlag:
        break
