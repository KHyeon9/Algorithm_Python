x1, x2, n = map(int, input().split())
# x1 - x2 -> 2 * (a_1....a_i)
diff = x1 - x2
# 변환값 구하기
total = diff // 2
# a_i는 전부 1이상 그래서 최소 총합은 n
# 따라서 위 조건이 안된다면 false
# diff % 2 == 0은 2배여야 같은 값이 증감되는 것을 보장
print("YES" if total >= n and diff % 2 == 0 else "NO")