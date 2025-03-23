from math import sqrt

def solution(direction, distance):
    global x, y
    distance = float(distance)
    diagonal = distance / sqrt(2)

    if direction == "N":
        y += distance
    elif direction == "S":
        y -= distance
    elif direction == "E":
        x += distance
    elif direction == "W":
        x -= distance
    elif direction == "NE":
        x += diagonal
        y += diagonal
    elif direction == "NW":
        x -= diagonal
        y += diagonal
    elif direction == "SE":
        x += diagonal
        y -= diagonal
    else:
        x -= diagonal
        y -= diagonal

t = int(input())
x, y = map(float, input().split())

for _ in range(t - 1):
    a, b = input().split()
    solution(a, b)

print(f"{x:.8f} {y:.8f}")