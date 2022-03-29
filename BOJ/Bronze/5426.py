from math import sqrt
for _ in range(int(input())):
    text = []
    s = input()
    l = int(sqrt(len(s)))
    for i in range(l):
        Slice = s[i * l:(i + 1) * l]
        text.append(Slice)
    for i in range(l - 1, -1, -1):
        for j in range(l):
            print(text[j][i], end='')
    print()