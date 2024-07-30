x, n = map(int, input().split())

num, res = 1, ""

while len(res) < n:
    res += str(num)
    num *= x

print(res[n - 1])