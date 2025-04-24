line = input()
robot = line.find("@")
box = line.find("#")
point = line.find("!")

if point > box > robot or robot > box > point:
    print(abs(point - robot) - 1)
else:
    print(-1)