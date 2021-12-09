n = int(input())
student = list(map(int, input().split()))
arr = []
for i in range(n):
    arr.insert(student[i], i + 1)
print(*arr[::-1])
