for _ in range(int(input())):
    a, b, c, d = input().split()
    b = int(b.split('/')[0])
    c = int(c.split('/')[0])

    print(a, end=" ")
    if b >= 2010 or c >= 1991:
        print("eligible")
    elif int(d) >= 41:
        print("ineligible")
    else:
        print("coach petitions")