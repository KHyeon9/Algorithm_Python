from math import ceil

mileage = 0

while True:
    line = list(input().split())

    if line[0] == "#":
        break

    if line[0] == "0":
        print(mileage)
        mileage = 0
        continue

    distance = int(line[2])
    if line[3] == "F":
        distance *= 2
    elif line[3] == "B":
        distance += ceil(distance * 0.5)
    else:
        distance = max(distance, 500)
    mileage += distance
