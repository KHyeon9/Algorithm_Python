from sys import stdin
input = stdin.readline
arr = [list(input().split()) for _ in range(int(input()))]
arr.sort(key=lambda x: int(x[1]))
name = sorted([i for i, j in arr if int(j) == int(arr[-1][1])])
print(name[0])