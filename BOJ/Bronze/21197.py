stopWatch = [int(input()) for _ in range(int(input()))]
if len(stopWatch) % 2 == 1:
    print("still running")
else:
    result = 0
    for i in range(0, len(stopWatch), 2):
        result += stopWatch[i + 1] - stopWatch[i]
    print(result)