n, m = map(int, input().split())
left = 1
right = m
d = 0

for i in range(int(input())):
    apple = int(input())
    if left <= apple <= right:
        continue
    if left > apple:
        d += left - apple
        right -= left - apple
        left = apple
    else:
        d += apple - right
        left += apple - right
        right = apple
print(d)