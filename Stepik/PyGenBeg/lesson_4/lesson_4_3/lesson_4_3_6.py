num_month = int(input())

if (num_month == 1 or num_month == 3 or num_month == 5 or num_month == 7 or
        num_month == 8 or num_month == 10 or num_month == 12):
    print(31)
elif num_month == 2:
    print(28)
else:
    print(30)
