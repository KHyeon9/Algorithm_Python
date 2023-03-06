n = int(input())
arr = [0] * (n + 1)
students = list(map(int, input().split()))

for s in students:
    arr[s] += 1
print(arr.index(1))
