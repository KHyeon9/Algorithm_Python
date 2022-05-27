i = 0

while 1:
    i += 1
    result = ""
    dead = False
    o, w = map(int, input().split())
    if o == w == 0:
        break
    while 1:
        play, n = input().split()
        n = int(n)
        if play == '#' and n == 0:
            break
        if play == 'F':
            w += n
        else:
            w -= n
        if w <= 0:
            dead = True
    if dead:
        result = f"{i} RIP"
    else:
        if o / 2 < w < o * 2:
            result = f"{i} :-)"
        else:
            result = f"{i} :-("
    print(result)
