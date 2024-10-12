n = int(input())
first_dice = list(map(int, input().split()))
second_dice = list(map(int, input().split()))

res = 0

for i in range(n):
    for j in range(n):
        if first_dice[i] > second_dice[j]:
            res += 1
        elif first_dice[i] < second_dice[j]:
            res -= 1

if res > 0:
    print("first")
elif res < 0:
    print("second")
else:
    print("tie")