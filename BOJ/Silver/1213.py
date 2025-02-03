count = {}
s = input()

for el in s:
    if el in count:
        count[el] += 1
    else:
        count[el] = 1

odd = 0
for val in count.values():
    if val % 2 == 1:
        odd += 1
    if odd > 1:
        print("I'm Sorry Hansoo")
        exit()

half = ""
middle = ""

for key, val in sorted(count.items()):
    if val % 2 == 1:
        middle = key

    if val != 1 and val % 2 == 1:
        val = val - 1

    half += key * (val // 2)
print(half + middle + half[::-1])

