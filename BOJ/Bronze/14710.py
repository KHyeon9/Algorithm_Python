h, m = map(int, input().split())
res = h % 30 * 12
print("O" if res == m else "X")