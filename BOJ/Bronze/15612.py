from sys import stdin
input = stdin.readline

def solution(n):
    if n == 0:
        return 0

    answer = ""

    while n:
        n, mod = divmod(n, 3)
        answer += str(mod)
    return answer[::-1]

for _ in range(int(input())):
    print(solution(int(input())))