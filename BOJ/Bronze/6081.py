n, q = map(int, input().split())

arr = [int(input()) for _ in range(n)]

for _ in range(q):
    s, e = map(int, input().split())
    print(sum(arr[s - 1: e]))