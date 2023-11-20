names = []

for _ in range(int(input())):
    name = input()

    if len(name) == 3:
        names.append(name)

print(sorted(names)[0])