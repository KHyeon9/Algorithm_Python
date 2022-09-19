for _ in range(int(input())):
    s = list(input().split())
    if s[0] == "Simon" and s[1] == "says":
        print(end=" ")
        print(*s[2:])
