n = int(input())
t = list(map(int, input().split()))
y = 0
m = 0

for i in range(n):
    y += t[i] // 30 * 10 + 10
    m += t[i] // 60 * 15 + 15

if y < m:
    print("Y", y)

elif y > m:
    print("M", m)

else:
    print("Y", "M", y)