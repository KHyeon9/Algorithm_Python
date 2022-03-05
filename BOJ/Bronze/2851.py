result, point = 0, 0
for _ in range(10):
    point += int(input())
    if abs(100 - result) >= abs(point - 100):
        result = point
print(result)