n = int(input())
level = list(map(int, input().split()))
answer = []

for l in level:
    if l >= 300:
        answer.append(1)
    elif l >= 275:
        answer.append(2)
    elif l >= 250:
        answer.append(3)
    else:
        answer.append(4)

print(*answer)