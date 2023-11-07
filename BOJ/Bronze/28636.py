res = 0

for _ in range(int(input())):
    m, s = map(int, input().split(":"))
    res += m * 60 + s

h = res // 3600 % 24
m = res // 60 % 60
s = res % 60
print(
    f"{h:02}:{m:02}:{s:02}"
)