paper = [229 * 324, 297 * 420, 210 * 297]
a, b, c = map(int, input().split())
answer = ((paper[0] * a + paper[1] * b) * 2 + paper[2] * c) * 1e-6
print("%.6f" % answer)
