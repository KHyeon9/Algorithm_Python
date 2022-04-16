n = int(input())
tropys = [int(input()) for _ in range(n)]
cnt1, cnt2 = 0, 0
tropy1, tropy2 = 0, 0
for i in tropys:
    if tropy1 < i:
        cnt1 += 1
        tropy1 = i

for i in tropys[::-1]:
    if tropy2 < i:
        cnt2 += 1
        tropy2 = i

print(cnt1)
print(cnt2)