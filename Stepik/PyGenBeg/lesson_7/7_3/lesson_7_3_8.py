# n = int(input())
#
# total = 0
# for i in range(1, n + 1):
#     if i ** 2 % 10 == 5:
#         total += i
#
# print(total)

n = int(input())

total = 0
for i in range(5, n + 1, 10):
    total += i

print(total)
