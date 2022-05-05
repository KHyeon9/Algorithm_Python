n, k = map(int, input().split())
distance = list(map(int, input().split()))
idx = distance
total_d = sum(distance)
total_m = 0
flag = False

if k // total_d % 2 != 0:
    distance.reverse()
    flag = True
k = k % total_d

for i in range(n):
    total_m += distance[i]
    if total_m > k:
        result = i
        break
if flag:
    print(n - result)
else:
    print(result + 1)