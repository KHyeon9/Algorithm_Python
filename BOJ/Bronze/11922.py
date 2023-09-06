symbols = {
    "A": 11,
    "K": 4,
    "Q": 3,
    "T": 10,
}

n, b = input().split()
res = 0

for _ in range(4 * int(n)):
    line = input()
    first_word = line[0]
    if first_word in symbols:
        res += symbols[first_word]
    else:
        second_word = line[1]
        if first_word == "J":
            res += 20 if second_word == b else 2
        elif first_word == "9" and second_word == b:
            res += 14
print(res)

