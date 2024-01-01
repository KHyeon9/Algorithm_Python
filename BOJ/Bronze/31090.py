for _ in range(int(input())):
    n = input()
    res = (int(n) + 1) % int(n[-2:])
    print("Good" if res == 0 else "Bye")