c = list(input())
ball = [1, 0, 0]

for i in range(len(c)):
    if c[i] == 'A':
        ball[0], ball[1] = ball[1], ball[0]

    elif c[i] == 'B':
        ball[1], ball[2] = ball[2], ball[1]

    else:
        ball[0], ball[2] = ball[2], ball[0]

for i in range(3):
    if ball[i] == 1:
        print(i + 1)