n = int(input())
n_len = len(str(n)) - 1
div = n / (10 ** n_len)

print(round(div) * (10 ** n_len))