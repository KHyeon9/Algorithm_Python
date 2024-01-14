arr = [
    "*x*",
    " xx",
    "* *"
]

n = int(input())

for  i in range(3):
    res = ""

    for e in arr[i]:
        res += e * n

    for _ in range(n):
        print(res)