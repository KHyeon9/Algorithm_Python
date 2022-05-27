n, l = input().split()
n = int(n)
cnt = n
i = 0
while cnt:
    i += 1
    if l in str(i):
        continue
    cnt -= 1
print(i)
