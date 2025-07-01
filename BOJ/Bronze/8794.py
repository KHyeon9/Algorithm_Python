from math import ceil

for _ in range(int(input())):
    n, m, l = map(int, input().split())
    # 월요일이 아닌경우 월요일로 만들기
    if l > 1:
        n -= m - l + 1
    # 소수점 올림
    print(ceil(n / m))