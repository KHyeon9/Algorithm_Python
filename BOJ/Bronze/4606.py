dic = {" ": "%20", "!": "%21", "$": "%24", "%": "%25",
       "(": "%28", ")": "%29", "*": "%2a"}

while 1:
    s = input()

    if s == "#":
        break

    res = ""

    for w in s:
        if w in dic:
            res += dic[w]
        else:
            res += w
    print(res)