n, k = map(int, input().split())
result = []
for _ in range(n):
    nums = list(input().split())
    for _ in range(k):
        s = ''
        for num in nums:
            s += num * k
        result.append(s)

for i in result:
    print(*i)