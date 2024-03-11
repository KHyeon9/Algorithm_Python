time = int(input())

if 30 >= time:
    print(round(time / 2, 1))
else:
    print(round(15 + (time - 30) * 1.5, 1))