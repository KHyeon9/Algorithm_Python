from math import ceil

n = int(input())
soldiers = list(map(int, input().split()))
train = soldiers.count(1)
half = ceil(len(soldiers) / 2)

res = half - train

print(max(res, 0))