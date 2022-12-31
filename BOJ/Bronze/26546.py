for _ in range(int(input())):
    s, start, end = input().split()
    print(s[0:int(start)] + s[int(end):])