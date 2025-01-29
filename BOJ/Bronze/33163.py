n = int(input())
s = list(input())

for i in range(n):
    if s[i] == "J":
        s[i] = "O"
    elif s[i] == "O":
        s[i] = "I"
    else:
        s[i] = "J"

print(*s, sep="")