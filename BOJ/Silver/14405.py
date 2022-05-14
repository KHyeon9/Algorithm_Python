pikachu = ["pi", "ka", "chu"]
s = input()
for i in pikachu:
    s = s.replace(i, ' ')
print("YES" if not s.strip() else "NO")