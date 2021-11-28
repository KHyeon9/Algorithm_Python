for i in range(int(input())):
    a, b, c = map(int, input().split())
    if max(a, b, c) >= a + b + c - max(a, b, c):
        print(f"Case #{i + 1}: invalid!")
    elif a == b == c:
        print(f"Case #{i + 1}: equilateral")
    elif a == b or a == c or b == c:
        print(f"Case #{i + 1}: isosceles")
    else:
        print(f"Case #{i + 1}: scalene")