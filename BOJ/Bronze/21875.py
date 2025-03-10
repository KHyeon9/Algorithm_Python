cell1 = input()
cell2 = input()

x = abs(ord(cell1[0]) - ord(cell2[0]))
y = abs(int(cell1[1]) - int(cell2[1]))
print(*sorted([x, y]))