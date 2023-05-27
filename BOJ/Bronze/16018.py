n = int(input())
parking_yesterday = input()
parking_today = input()
res = 0

for i in range(n):
    if parking_yesterday[i] == parking_today[i] == 'C':
        res += 1

print(res)