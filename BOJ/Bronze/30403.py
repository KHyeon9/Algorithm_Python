rainbow_lower = "roygbiv"
rainbow_upper = rainbow_lower.upper()
lower_arr, upper_arr = [], []

n = int(input())
line = input()

for el in line:
    if el in rainbow_lower and el not in lower_arr:
        lower_arr.append(el)
    if el in rainbow_upper and el not in upper_arr:
        upper_arr.append(el)
lower_len, upper_len = len(lower_arr), len(upper_arr)

if lower_len == upper_len == 7:
    print("YeS")
elif lower_len == 7:
    print("yes")
elif upper_len == 7:
    print("YES")
else:
    print("NO!")