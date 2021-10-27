x, y, z = map(int, input().split())
x2, y2, z2 = map(int, input().split())

if x <= x2 and y <= y2 and z <= z2:
    print("A")
elif x / 2 <= x2 and y <= y2 and z <= z2:
    print("B")
elif y <= y2 and z <= z2:
    print("C")
elif y / 2 <= y2 and z / 2 <= z2:
    print("D")
else:
    print("E")