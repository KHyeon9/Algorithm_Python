holes_word = {'A': 1, 'B': 2, 'D': 1, 'O': 1, 'P': 1,
              'Q': 1, "R": 1, }

for _ in range(int(input())):
    s = input()
    res = 0
    for w in s:
        if w in holes_word:
            res += holes_word[w]

    print(res)
