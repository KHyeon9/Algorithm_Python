rotate = ['I', 'O', 'S', 'H', 'Z', 'X', 'N']
flag = True
for w in input():
    if w not in rotate:
        flag = False
print("YES" if flag else "NO")