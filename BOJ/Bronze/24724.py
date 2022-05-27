import sys
input = sys.stdin.readline

for tc in range(1, int(input()) + 1):
    n = int(input())
    v_limit, w_limit = map(int, input().split())
    for _ in range(n):
        u, v = map(int, input().split())
    print(f"Material Management {tc}")
    print("Classification ---- End!")