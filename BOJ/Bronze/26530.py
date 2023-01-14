for _ in range(int(input())):
    n = int(input())
    result = 0

    for i in range(n):
        name, cnt, price = input().split()
        cnt = int(cnt)
        if price[0] == '.':
            price = '0' + price
        price = float(price)
        result += cnt * price
    print("$%.2f" % result)