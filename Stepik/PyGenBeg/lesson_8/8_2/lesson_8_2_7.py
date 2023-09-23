n = 1729

count_sol = 0
while count_sol < 5:
    count = 0
    for x in range(1, int(n ** (1 / 3) + 1)):
        for y in range(x, int(n ** (1 / 3) + 1)):
            if x ** 3 + y ** 3 == n:
                # print(x, y, n)
                count += 1
            if count == 2:
                break
        if count == 2:
            count_sol += 1
            break
    if count == 2:
        print(n)
    n += 1
