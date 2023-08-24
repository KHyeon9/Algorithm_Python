arr = ["N", "S", "W", "E"]
n = int(input())
s = input()
cnt = 0

for a in arr:
    if s.count(a) > cnt:
        cnt = s.count(a)
print(n - cnt)