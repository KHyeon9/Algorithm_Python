n = input()
cnt = 0
while len(n) > 1:
    num = 1
    for i in n:
        num *= int(i)
    cnt += 1
    n = str(num)
print(cnt)