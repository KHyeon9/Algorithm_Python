def solution(o, a, k):
    for i in range(1, o // a + 1):
        for j in range(1, o // k + 1):
            if a * i + k * j == o:
                return True
    return False

o, a, k = map(int, input().split())
print(1 if solution(o, a, k) else 0)