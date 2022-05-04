money = int(input())
stock = list(map(int, input().split()))

joon_cnt, joon_money = 0, money
sung_cnt, sung_money = 0, money

for i in stock:
    if joon_money >= i:
        joon_cnt += joon_money // i
        joon_money %= i
for i in range(len(stock) - 3):
    if stock[i] > stock[i + 1] > stock[i + 2] > stock[i + 3]:
        sung_cnt += sung_money // stock[i + 3]
        sung_money %= stock[i + 3]
    if stock[i] < stock[i + 1] < stock[i + 2] < stock[i + 3]:
        sung_money += stock[i + 3] * sung_cnt
        sung_cnt = 0

joon_result = (joon_cnt * stock[-1]) + joon_money
sung_result = (sung_cnt * stock[-1]) + sung_money

if joon_result > sung_result:
    print("BNP")
elif joon_result < sung_result:
    print("TIMING")
else:
    print("SAMESAME")