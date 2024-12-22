x, y = map(int, input().split())
d = int(input())

total = x * 100 + y

big = (total / 4) + (d / 2)
small = (total / 4) - (d / 2)

print(f"{int(big // 100)} {int(big % 100)}")
print(f"{int(small // 100)} {int(small % 100)}")