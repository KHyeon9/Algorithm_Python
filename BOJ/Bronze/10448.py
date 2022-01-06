arr = [i * (i + 1) // 2 for i in range(1, 45)]
def sol(num):
    for i in arr:
        for j in arr:
            for k in arr:
                if i + j + k == num:
                    return 1
    return 0


for _ in range(int(input())):
    n = int(input())
    print(sol(n))