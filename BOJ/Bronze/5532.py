import math

L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

K = math.ceil(A / C)
M = math.ceil(B / D)


print(L - max(K, M))
