n = int(input())
s = input()

if len(s) > n:
    print("Impossible")
else:
    res = 0
    for w in s:
        res += ord(w) - ord('a') + 1
    print(res)