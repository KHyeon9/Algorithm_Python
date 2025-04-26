from sys import stdin
input = stdin.readline

n, item = input().split()
n = int(n)
res = 0

for _ in range(n):
    name, cnt = input().split()
    name_arr = name.split("_")

    if item in name_arr:
        res += int(cnt)
print(res)