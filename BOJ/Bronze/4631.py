test_case = 0

while True:
    n = int(input())
    test_case += 1

    if n == 0:
        break

    name1, name2 = [], []

    for i in range(n):
        name = input()
        if i % 2 == 0:
            name1.append(name)
        else:
            name2.append(name)

    total_name = name1 + name2[::-1]

    print(f"SET {test_case}")
    for el in total_name:
        print(el)