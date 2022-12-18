cnt = 0
while 1:
    try:
        s = input()
        if s == "gum gum for jay jay":
            cnt += 1
    except EOFError:
        break
