s = input()

flag = False
for c in s:
    if c in '0123456789':
        flag = True
        break

if flag:
    print('Цифра')
else:
    print('Цифр нет')
