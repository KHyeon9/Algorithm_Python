def solution(n):
    if n <= 1:
        return n
    if n % 2 != 0:
        return 1 - solution(n // 2)
    else:
        return solution(n // 2)


N = int(input())
print(solution(N - 1))