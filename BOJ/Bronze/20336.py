import random
t = int(input())
arr = [list(input().split()) for _ in range(t)]
n = random.randrange(0, t)
res = arr[n]
print(res[0])
for l in res[1:]:
    print(l)