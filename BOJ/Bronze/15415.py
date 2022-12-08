w = int(input())
result = 0

for _ in range(int(input())):
    wi, li = map(int, input().split())
    result += wi * li
print(result // w)