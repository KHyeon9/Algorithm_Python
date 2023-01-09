n = int(input())
li = list(map(int, input().split()))
result = 0
for i in li:
    result += min(i, n)
print(result)

