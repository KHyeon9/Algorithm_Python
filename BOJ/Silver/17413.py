s = input()
result = ""
stack = ""
flag = False
for word in s:
    if not flag:
        if word == '<':
            flag = True
            result += stack[::-1]
            stack = ""
            stack += word
        elif word == ' ':
            result += stack[::-1] + word
            stack = ""
        else:
            stack += word
    else:
        stack += word
        if word == '>':
            flag = False
            result += stack
            stack = ""

print(result + stack[::-1])







