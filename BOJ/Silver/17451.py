n = int(input())
speed = list(map(int, input().split()))[::-1]
answer = 0
for i in range(n):
    if answer <= speed[i]:
        answer = speed[i]
    else:
        if answer % speed[i]:
            answer = (answer // speed[i] + 1) * speed[i]
print(answer)