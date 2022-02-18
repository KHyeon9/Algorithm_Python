for _ in range(int(input())):
    n = int(input())
    answer = 0
    for i in range(2, min(n + 1, 65)):
        s = []
        num = n
        while num:
            s.append(num % i)
            num //= i
        if s == s[::-1]:
            answer = 1
    print(answer)

