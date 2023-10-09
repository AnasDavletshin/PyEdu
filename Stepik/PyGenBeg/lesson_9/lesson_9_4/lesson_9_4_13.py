s = input()

max_count = 0
max_char = s[0]
for ch in s:
    char_count = s.count(ch)
    if char_count >= max_count:
        max_count = char_count
        max_char = ch
print(max_char)
