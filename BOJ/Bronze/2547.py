t = int(input())
for _ in range(t):
    arr = []
    e = input()
    n = int(input())
    for _ in range(n):
        arr.append(int(input()))
    if sum(arr) % n == 0:
        print("YES")
    else:
        print("NO")