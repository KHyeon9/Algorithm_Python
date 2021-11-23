a, b = map(int, input().split())
m = int(input())
num = list(map(int, input().split()))
num.reverse()
n = 0
r = []
for i in range(m):
    n += num[i] * (a ** i)
while n != 0:
    r.append(n % b)
    n //= b
print(*r[::-1])
