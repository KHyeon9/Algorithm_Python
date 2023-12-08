while True:
    n = int(input())

    if n == 0:
        break

    nums = [int(input()) for _ in range(n)][::-1]
    for num in nums:
        print(num)
    print(0)
