t = 1

while True:
    n = int(input())

    if n == 0:
        break

    month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul",
             "Aug", "Sep", "Oct", "Nov", "Dec"]
    graph = [0] * 12

    for _ in range(n):
        d, m, y = input().split()
        graph[int(m) - 1] += 1

    print(f"Case #{t}:")

    for i in range(12):
        print(f"{month[i]}:" + "*" * graph[i])

    t += 1