for t in range(int(input())):
    b = int(input())
    s = input().replace('O', '0').replace('I', '1')
    res = ""
    for i in range(b):
        res += chr(int(s[8 * i:8 * (i + 1)], 2))
    print(f"Case #{t + 1}: {res}")