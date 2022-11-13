for _ in range(int(input())):
    n, x, y = map(int, input().split())
    prob = list(map(int, input().split()))
    not_prob = False
    not_color = False
    if prob[0] == x:
        not_prob = True
    if prob[n - 1] == y:
        not_color = True

    if not_prob and not_color:
        print("BOTH")
    elif not_prob and not not_color:
        print("EASY")
    elif not not_prob and not_color:
        print("HARD")
    else:
        print("OKAY")
