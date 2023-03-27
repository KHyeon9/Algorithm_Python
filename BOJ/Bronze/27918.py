x, y = 0, 0

for _ in range(int(input())):
    win = input()
    if win == 'D':
        x += 1
    else:
        y += 1

    if x == 2 + y or y == 2 + x:
        break
print(f"{x}:{y}")