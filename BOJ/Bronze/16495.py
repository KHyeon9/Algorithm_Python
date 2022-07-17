n = input()
res = 0
for i in range(len(n)):
    alpa = ord(n[i]) - 64
    res += alpa * (26 ** (len(n) - i - 1))
print(res)