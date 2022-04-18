n = int(input())

j = "7890123456"
g = "JKLABCDEFGHI"

print(g[n % 12 - 1] + j[n % 10 - 1])
