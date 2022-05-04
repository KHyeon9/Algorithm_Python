n = int(input())
gym = sorted(list(map(int, input().split())))
musle = 0
if n % 2:
    musle = gym[-1]
    for i in range(n // 2):
        less = gym[i] + gym[-2 - i]
        musle = max(musle, less)
else:
    for i in range(n // 2):
        less = gym[i] + gym[-1 - i]
        musle = max(musle, less)
print(musle)