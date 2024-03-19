n = int(input())
s1 = input()
s2 = input()
res = 0

for i in range(n):
    if s1[i] != s2[i]:
        res += 1

print(res)