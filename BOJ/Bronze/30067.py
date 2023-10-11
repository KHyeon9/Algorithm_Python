arr = [int(input()) for _ in range(10)]
sum_arr = sum(arr)

for n in arr:
    if sum_arr - n == n:
        print(n)
        break
