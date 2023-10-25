n = int(input())
s = input()
res = 0

for i in range(n):
    if i % 2 == 0 and s[i] != 'I':
        res += 1
    elif i % 2 == 1 and s[i] != 'O':
        res += 1

print(res)
