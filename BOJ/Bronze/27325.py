n = int(input())
s = input()
ball = 1
res = 0
for el in s:
    if el == 'L':
        ball -= 1 if ball > 1 else 0
    else:
        ball += 1 if ball < 3 else 0
        if ball >= 3:
            res += 1
print(res)

