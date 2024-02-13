n, a = map(int, input().split())
res = 0

for num in list(map(int, input().split())):
    res += num // a

print(res)