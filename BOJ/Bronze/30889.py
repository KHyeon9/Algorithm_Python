seats = [['.' for _ in range(20)] for _ in range(10)]

for _ in range(int(input())):
    line = input()
    x = int(line[1:]) - 1
    y = ord(line[0]) - ord('A')
    seats[y][x] = 'o'

for line in seats:
    print(*line, sep='')

