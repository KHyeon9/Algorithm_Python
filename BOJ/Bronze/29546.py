files = [input() for _ in range(int(input()))]
for _ in range(int(input())):
    start, end = map(int, input().split())

    for i in range(start - 1, end):
        print(files[i])
