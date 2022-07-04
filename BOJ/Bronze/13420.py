for _ in range(int(input())):
    s = input().split()
    a, b, c = int(s[0]), int(s[2]), int(s[4])
    x = s[1]
    if x == '+':
        res = a + b
    elif x == '-':
        res = a - b
    elif x == '*':
        res = a * b
    elif x == '/':
        res = a // b
    print("correct" if res == c else "wrong answer")
