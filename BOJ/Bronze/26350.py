for _ in range(int(input())):
    coin = sorted(list(map(int, input().split()))[1:])
    flag = True

    for i in range(1, len(coin)):
        if coin[i - 1] * 2 > coin[i]:
            flag = False
            break

    print(f"Denominations: " + " ".join(map(str, coin)))
    print("Good coin denominations!" if flag else "Bad coin denominations!")
    print()