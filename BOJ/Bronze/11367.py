def grade(n):
    if n >= 97:
        return "A+"
    elif n >= 90:
        return "A"
    elif n >= 87:
        return "B+"
    elif n >= 80:
        return "B"
    elif n >= 77:
        return "C+"
    elif n >= 70:
        return "C"
    elif n >= 67:
        return "D+"
    elif n >= 60:
        return "D"
    else:
        return "F"

for _ in range(int(input())):
    name, test = input().split()
    print(name, grade(int(test)))