a, b, c = map(int, input().split())
result = 0
n = int(input())
for _ in range(n):
    r = 0
    for i in range(3):
        n1, n2, n3 = map(int, input().split())
        r += n1 * a + n2 * b + n3 * c
    result = max(result, r)
print(result)