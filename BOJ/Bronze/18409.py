n = int(input())
s = input()
res = 0
for i in s:
    if i in ['a', 'i', 'u', 'e', 'o']:
        res += 1
print(res)
