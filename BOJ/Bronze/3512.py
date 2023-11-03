dic = {"bedroom": 0, "balcony": 0}
total = 0
n, c = map(int, input().split())

for _ in range(n):
    a, t = input().split()
    a = int(a)
    total += a
    if t not in dic:
        dic[t] = a
    else:
        dic[t] += a

print(total)
print(dic["bedroom"])
print(c * (total - dic["balcony"] / 2))