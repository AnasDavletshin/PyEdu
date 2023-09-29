s = input()

v_total = 0
c_total = 0
for c in s:
    if c in 'ауоыиэяюёеАУОЫИЭЯЮЁЕ':
        v_total += 1
    elif c in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
        c_total += 1

print('Количество гласных букв равно ' + str(v_total))
print('Количество согласных букв равно ' + str(c_total))
