res, max_pay = "", 0
for _ in range(int(input())):
    pay, name, country = input().split()

    if max_pay < int(pay) and country == "Russia":
        max_pay = int(pay)
        res = name

print(res)