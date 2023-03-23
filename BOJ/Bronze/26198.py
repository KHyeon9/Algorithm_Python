dic = {"I": 1, "V": 5, "X": 10, "L": 50,
       "C": 100, "D": 500, "M": 1000}

for _ in range(int(input())):
    s = input()
    res = 0
    for i in s:
        if i in dic:
            res += dic[i]
    print(res)
