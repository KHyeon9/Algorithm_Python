n = int(input())
s = set(input())
words = "ABCED"
cnt = 0

for w in s:
    if w in words:
        cnt += 1

print("Yes" if cnt >= 3 else "No")
