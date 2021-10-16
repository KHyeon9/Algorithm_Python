a, b = map(int, input().split())
Max = max(a, b)
Min = min(a, b)
result = (a + b) * (Max - Min + 1) // 2
print(result)