br, bc = map(int, input().split())
dr, dc = map(int, input().split())
jr, jc = map(int, input().split())

r1 = max(abs(br - jr), abs(bc - jc))
r2 = abs(dr - jr) + abs(dc - jc)

if r1 > r2:
    print("daisy")

elif r1 < r2:
    print("bessie")

else:
    print("tie")