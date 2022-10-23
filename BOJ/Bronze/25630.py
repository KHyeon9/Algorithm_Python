n = int(input())
s = input()
s1 = s[:n//2][::-1]
s2 = s[n//2:] if n % 2 == 0 else s[n//2 + 1:]
cnt = 0
for i in range(n // 2):
    if s1[i] != s2[i]:
        cnt += 1
print(cnt)