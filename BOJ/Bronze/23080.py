n = int(input())
s = input()
res = ""
for i in range(0, len(s), n):
    res += s[i]
print(res)
