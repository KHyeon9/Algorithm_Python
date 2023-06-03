s = "SciComLove"

for _ in range(int(input()) % 10):
    s = s[1:] + s[0]
print(s)