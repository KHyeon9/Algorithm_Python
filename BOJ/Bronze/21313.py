n = int(input())
arr = [1, 2] * (n // 2)
if n % 2 == 1:
    arr.append(3)
print(*arr)