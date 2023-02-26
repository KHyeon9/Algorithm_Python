def sol(a, b):
    if a == 0 or b == 0:
        return "AXIS";
    elif a > 0 and b > 0:
        return "Q1"
    elif a < 0 < b:
        return "Q2"
    elif a < 0 and b < 0:
        return "Q3"
    elif a > 0 > b:
        return "Q4"


while 1:
    try:
        x, y = map(float, input().split())
        print(sol(x, y))
    except EOFError:
        break
