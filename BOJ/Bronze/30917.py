x, num = "A", 1
res = 0

while True:
    print(f"? {x} {num}")
    n = int(input())

    if n == 1:
        res += num
        if x == "B":
            print(f"! {res}")
            break

        x, num = "B", 1
    else:
        num += 1
