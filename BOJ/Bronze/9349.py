for _ in range(int(input())):
    n, k = map(int, input().split())
    # 간격은 k - 1
    # 총 빈칸의 갯수는 빈대를 뺀 수
    print((n - k) // (k - 1))