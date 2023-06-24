n, k = map(int, input().split())
s = input()
res = ""

for i in range(n):
    if i + 1 >= k:
        if s[i].isupper():
            res += s[i].lower()
        else:
            res += s[i].upper()
    else:
        res += s[i]
print(res)