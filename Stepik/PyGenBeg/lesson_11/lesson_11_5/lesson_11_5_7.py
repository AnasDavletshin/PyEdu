numbers = input().split('.')
for n in numbers:
    if not (0 <= int(n) <= 255):
        print('НЕТ')
        break
else:
    print('ДА')
