vowels = "aeiou"
for _ in range(int(input())):
    line = input()
    res = 0

    for v in vowels:
        res += line.count(v)

    print(f"The number of vowels in {line} is {res}.")