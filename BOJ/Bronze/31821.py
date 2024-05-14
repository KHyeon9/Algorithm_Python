price = [int(input()) for _ in range(int(input()))]
res = 0

for _ in range(int(input())):
    res += price[int(input()) - 1]

print(res)