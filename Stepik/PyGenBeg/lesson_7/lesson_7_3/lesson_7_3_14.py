flag = True
for _ in range(10):
    if int(input()) % 2 == 1:
        flag = False

if flag:
    print('YES')
else:
    print('NO')
