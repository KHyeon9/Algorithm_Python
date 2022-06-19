for _ in range(int(input())):
    n = int(input())
    pow_n = str(n ** 2)
    l = len(str(n))
    if int(pow_n[-l:]) == n:
        print("YES")
    else:
        print("NO")