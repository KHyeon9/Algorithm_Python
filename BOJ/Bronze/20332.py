n = int(input())
prize_money = list(map(int, input().split()))
print("yes" if sum(prize_money) % 3 == 0 else "no")
