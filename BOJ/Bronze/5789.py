for _ in range(int(input())):
    s = input()
    result = "Do-it-Not"

    if s[len(s) // 2 - 1] == s[len(s) // 2]:
        result = "Do-it"

    print(result)
