while 1:
    cards = list(input().split())
    if cards[0] == "#":
        break
    Cheryl, Tania = 0, 0

    for n in cards[:-1]:
        n = int(n) if n != "A" else n
        if n == "A" or n % 2 == 1:
            Cheryl += 1
        elif n % 2 == 0:
            Tania += 1

    if Cheryl > Tania:
        print("Cheryl")
    elif Cheryl < Tania:
        print("Tania")
    else:
        print("Draw")