n, k = map(int, input().split())
sum_problems = sum([int(input()) for _ in range(k)])
print(f"{(sum_problems - (n - k) * 3) / n} {(sum_problems + (n - k) * 3) / n}")