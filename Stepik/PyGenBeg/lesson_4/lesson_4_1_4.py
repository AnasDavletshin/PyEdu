password = input()
password_confirmation = input()

if password == password_confirmation:
    print('Пароль принят')
else:
    print('Пароль не принят')
