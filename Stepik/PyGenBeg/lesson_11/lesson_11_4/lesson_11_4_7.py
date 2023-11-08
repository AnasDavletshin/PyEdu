n = int(input())

strings = []
for _ in range(n):
    strings.append(input())

k = int(input())

search_queries = []
for _ in range(k):
    search_queries.append(input().lower())

for s in strings:
    for sq in search_queries:
        if sq not in s.lower():
            flag = False
            break
    else:
        print(s)
