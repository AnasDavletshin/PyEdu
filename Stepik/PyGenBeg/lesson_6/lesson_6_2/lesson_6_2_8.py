city1 = input()
city2 = input()
city3 = input()

len1 = len(city1)
len2 = len(city2)
len3 = len(city3)

min_len = min(len1, len2, len3)
if min_len == len1:
    print(city1)
elif min_len == len2:
    print(city2)
else:
    print(city3)

max_len = max(len1, len2, len3)
if max_len == len1:
    print(city1)
elif max_len == len2:
    print(city2)
else:
    print(city3)
