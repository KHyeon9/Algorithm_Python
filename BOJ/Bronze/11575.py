for _ in range(int(input())):
    a, b = map(int, input().split())
    s = input()
    res = ""
    for i in s:
        x = ord(i) - ord('A')
        ac = (a * x + b) % 26
        res += chr(ac + ord('A'))
    print(res)
