alpa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
res = []

while True:
    line1 = input()

    if line1 == "ENDOFINPUT":
        break

    decode = ""
    s = input().strip()

    for w in s:
        if w not in alpa:
            decode += w
            continue
        decode += alpa[(alpa.find(w) - 5) % 26]

    input()
    print(decode)