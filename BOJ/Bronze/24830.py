temp = 1

for _ in range(int(input())):
    a, op, b = input().split()
    a, b = int(a), int(b)

    if op == "+":
        temp = a + b - temp
    elif op == "-":
        temp = (a - b) * temp
    elif op == "*":
        temp = (a * b) ** 2
    else:
        temp = (a + 1) // 2 if a % 2 == 1 else a // 2

    print(temp)
