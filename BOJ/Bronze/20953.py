from sys import stdin
input = stdin.readline

def dolmen(n1, n2):
    return (n1 + n2 - 1) * (n1 + n2) // 2 * (n1 + n2)

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(dolmen(a, b))