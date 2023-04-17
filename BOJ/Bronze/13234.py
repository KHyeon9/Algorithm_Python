s = list(input().split())

if s[1] == "AND":
    if s[0] == "false" or s[2] == "false":
        print("false")
    else:
        print("true")
else:
    if s[0] == "false" and s[2] == "false":
        print("false")
    else:
        print("true")