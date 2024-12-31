n = int(input())
total = list(input().split())
use = list(input().split())

for el in total:
    if el not in use:
        print(el)
        break