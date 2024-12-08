def solution(n1, n2):
    out = (n1 - n2 + 43) % 43
    inner = (n2 - n1 + 43) % 43

    if out > inner:
        return "Inner circle line"
    return "Outer circle line"


for _ in range(int(input())):
    a, b = map(int, input().split())
    print(solution(a, b))