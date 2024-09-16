a = int(input())
w, v = map(int, input().split())

print(1 if a * v <= w else 0)