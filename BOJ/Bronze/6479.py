from math import factorial
while True:
    n = int(input())
    if n == 0:
        break
    input()

    res = {f"{i}": 0 for i in range(10)}
    fac_num = str(factorial(n))
    set_fac_num = set(fac_num)

    for i in set_fac_num:
        res[i] = fac_num.count(i)

    print(f"{n}! --")
    for k, v in res.items():
        print(f"   ({k}){v:5}", end=" ")
        if k == "4":
            print()
    print()
