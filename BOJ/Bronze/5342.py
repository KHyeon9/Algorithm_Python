cost = {"Paper": 57.99, "Printer": 120.50, "Planners": 31.25,
        "Binders": 22.50, "Calendar": 10.95, "Notebooks": 	11.20,
        "Ink": 	66.95}

res = 0

while 1:
    s = input()

    if s == "EOI":
        break

    res += cost[s]

print(f"${res}")