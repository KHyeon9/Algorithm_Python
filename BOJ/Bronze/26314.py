vowel = "aeiou"
for _ in range(int(input())):
    s = input()
    res = 0

    for i in vowel:
        res += s.count(i)

    print(s)

    if res > len(s) - res:
        print(1)
    else:
        print(0)