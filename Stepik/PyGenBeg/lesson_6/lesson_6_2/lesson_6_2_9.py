s1 = input()
s2 = input()
s3 = input()

len1 = len(s1)
len2 = len(s2)
len3 = len(s3)

if (
        len1 + len2 == 2 * len3 or
        len1 + len3 == 2 * len2 or
        len2 + len3 == 2 * len1
):
    print('YES')
else:
    print('NO')
