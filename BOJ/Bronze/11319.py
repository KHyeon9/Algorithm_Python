vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

for _ in range(int(input())):
    s = input()
    r1, r2 = 0, 0

    for i in s:
        if i == ' ':
            continue
        elif i in vowels:
            r1 += 1
        else:
            r2 += 1
    print(r2, r1)
