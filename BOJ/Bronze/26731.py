def sol(words):
    al = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for w in al:
        if w not in words:
            return w

s = input()
print(sol(s))
