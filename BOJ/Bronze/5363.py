for _ in range(int(input())):
    s = list(input().split())
    print(*s[2:] + s[:2])