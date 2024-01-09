x, y, z = sorted(list(map(int, input().split())))

if y == 0:
    print(f"{z}00")
elif x == 0:
    print(f"{y}0{z}")
else:
    print(f"{x}{y}{z}")


