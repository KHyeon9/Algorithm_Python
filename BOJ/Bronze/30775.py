from math import ceil
n, k = map(int, input().split())
n_list = list(map(int, input().split()))

print(ceil(sum(n_list) / n))