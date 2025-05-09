n, m = map(int, input().split())

if m <= 26:
    observation = chr(ord('A') + m - 1)
else:
    m -= 27
    first = chr(ord('a') + m // 26)
    second = chr(ord('a') + m % 26)
    observation = first + second

print(f"SN {n}{observation}")