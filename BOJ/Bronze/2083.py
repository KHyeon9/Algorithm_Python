while 1:
    name, age, weight = input().split()
    age, weight = int(age), int(weight)
    if name == '#' and age == weight == 0:
        break
    res = "Junior"
    if age > 17 or weight >= 80:
        res = "Senior"
    print(f"{name} {res}")