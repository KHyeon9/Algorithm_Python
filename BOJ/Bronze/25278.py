temp, oxy, oce = -30, 0, 0
for _ in range(int(input())):
    type, change = input().split()
    change = int(change[1])

    if type == "temperature":
        temp += change
    elif type == "oxygen":
        oxy += change
    elif type == "ocean":
        oce += change

print("liveable"
      if temp >= 8 and oxy >= 14 and oce >= 9
      else "not liveable")

