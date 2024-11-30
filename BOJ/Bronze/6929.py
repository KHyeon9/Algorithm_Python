n = int(input())
res = []
for i in range(1, n, 2):
    res.append("*" * i + " " * ((n - i) * 2) + "*" * i)

for el in res:
    print(el)
print("*" * n * 2)
for el in res[::-1]:
    print(el)



