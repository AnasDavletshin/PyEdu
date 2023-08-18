c1 = input()
c2 = input()

if c1 == 'красный' and c2 == 'синий' or c1 == 'синий' and c2 == 'красный':
    print('фиолетовый')
elif c1 == 'красный' and c2 == 'желтый' or c1 == 'желтый' and c2 == 'красный':
    print('оранжевый')
elif c1 == 'синий' and c2 == 'желтый' or c1 == 'желтый' and c2 == 'синий':
    print('зеленый')
elif (c1 == 'красный' or c1 == 'синий' or c1 == 'желтый') and c1 == c2:
    print(c1)
else:
    print('ошибка цвета')
