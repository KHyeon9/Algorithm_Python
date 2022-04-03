s = ''
while 1:
    try:
        s += input()
    except EOFError:
        break

s = sum(map(int, s.split(',')))
print(s)

