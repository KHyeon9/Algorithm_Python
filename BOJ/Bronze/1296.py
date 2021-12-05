s = input()
n = int(input())
names = sorted([input() for _ in range(n)])
MAX, result = 0, 0
for i in range(n):
    L = s.count('L') + names[i].count('L')
    O = s.count('O') + names[i].count('O')
    V = s.count('V') + names[i].count('V')
    E = s.count('E') + names[i].count('E')
    win = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100
    if MAX < win:
        MAX = win
        result = i
print(names[result])