from math import sqrt

for _ in range(int(input())):
    a, b, c = map(float, input().split())
    res1 = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    res2 = (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    print(f"{res1:.3f}, {res2:.3f}")