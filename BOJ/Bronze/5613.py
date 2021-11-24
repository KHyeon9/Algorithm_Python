r = 0
t = 0
c = '+'

while 1:
    n = input()
    if n == '=':
        break

    if t % 2 == 0:
        if c == '+':
            r += int(n)

        elif c == '-':
            r -= int(n)

        elif c == '*':
            r *= int(n)

        elif c == '/':
            r //= int(n)

    else:
        c = n

    t += 1
print(r)