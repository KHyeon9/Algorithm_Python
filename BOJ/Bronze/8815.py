q = ["A", "B", "C", "B", "C", "D", "C", "D", "A", "D", "A", "B"]
for _ in range(int(input())):
    n = int(input())
    print(q[n % len(q) - 1])
