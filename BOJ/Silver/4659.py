al = "aeiou"

while 1:
    s = input()

    if s == "end":
        break

    flag = False
    for i in range(len(s)):
        if s[i] in al:
            flag = True
        if i > 1:
            if s[i] in al and s[i - 1] in al and s[i - 2] in al:
                flag = False
                break
            if s[i] not in al and s[i - 1] not in al and s[i - 2] not in al:
                flag = False
                break
        if i > 0:
            if s[i] == s[i - 1] and s[i] != 'e' and s[i] != 'o':
                flag = False
                break
    if flag:
        print(f"<{s}> is acceptable.")
    else:
        print(f"<{s}> is not acceptable.")
