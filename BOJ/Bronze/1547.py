n = int(input())
ball = [0, 1, 0, 0]

for _ in range(n):
    a, b = map(int, input().split())
    temp = 0

    temp = ball[a]
    ball[a] = ball[b]
    ball[b] = temp


for i in range(4):
    if ball[i] == 1:
        print(i)
        break