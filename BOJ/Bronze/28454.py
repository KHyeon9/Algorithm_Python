now_date = list(map(int, input().split('-')))
res = 0

for _ in range(int(input())):
    gift_date = list(map(int, input().split('-')))

    if gift_date >= now_date:
        res += 1

print(res)