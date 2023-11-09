for _ in range(int(input())):
    bit = input()
    res = 0
    for i in range(0, len(bit), 8):
        cnt = bit[i:i + 7].count("1")

        if cnt % 2 != int(bit[i + 7]):
            res += 1

    print(res)