a = list(map(int, input().split()))
b = list(map(lambda x: x ** 2, a))
print(sum(b) % 10)
