# n = int(input())
# total = 0
# while n > 0:
#     if n >= 25:
#         k = 25
#     elif n >= 10:
#         k = 10
#     elif n >= 5:
#         k = 5
#     else:
#         k = 1
#     total += (n // k)
#     n %= k
# print(total)

n = int(input())
total = 0
for k in (25, 10, 5, 1):
    total += (n // k)
    n %= k
print(total)
