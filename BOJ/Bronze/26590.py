s1, s2 = input().split()
res = ""
for i in range(min(len(s1), len(s2))):
    if i % 2 == 0:
        res += s1[i]
    else:
        res += s2[i]

print(res)

