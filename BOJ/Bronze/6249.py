n, p, h = map(int, input().split())

for i in range(n):
    d = int(input())

    if d > h:
        h = d
        p = d
        print(f"BBTV: Dollar reached {h} Oshloobs, A record!")
    else:
        if p > d:
            print(f"NTV: Dollar dropped by {p - d} Oshloobs")
            p = d
        else:
            p = d