n = int(input())
candy = list(map(int, input().split()))
res = 0
odd = []

for c in candy:
    if c % 2 == 0:
        res += c
    else:
        odd.append(c)

odd.sort(reverse=True)

if len(odd) % 2 == 0:
    res += sum(odd)
else:
    res += sum(odd[:-1])
print(res)