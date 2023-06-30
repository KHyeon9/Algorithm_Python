arr = [0] * 10001
gold_day, cnt = 1, 0
for i in range(1, 10001):
    arr[i] = arr[i - 1] + gold_day
    cnt += 1
    if gold_day == cnt:
        cnt = 0
        gold_day += 1

while True:
    n = int(input())
    if n == 0:
        break
    print(n, arr[n])