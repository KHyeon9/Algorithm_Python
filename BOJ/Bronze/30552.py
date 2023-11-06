res_arr = []

for _ in range(int(input())):
    callout = input()

    if callout == "Present!":
        res_arr.pop()
        continue
    res_arr.append(callout)

if not res_arr:
    print("No Absences")

for r in res_arr:
    print(r)