s = input()
flag = True

for word in ['M', 'O', 'B', 'I', 'S']:
    if word not in s:
        flag = False
        break
print("YES" if flag else "NO")