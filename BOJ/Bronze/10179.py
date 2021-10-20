t = int(input())

for i in range(t):
    result = float(input())

    print("$%.2f" % round(result * 0.8, 2))