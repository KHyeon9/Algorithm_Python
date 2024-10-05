box, cnt = 0, 0

for _ in range(int(input())):
    box_type, w, h, l = input().split()
    w, h, l = int(w), int(h), int(l)

    if box_type == 'A':
        cnt += (w // 12) * (h // 12) * (l // 12)
        box += 1000
    else:
        box += 6000

box += cnt * 500
price = cnt * 4000

print(box)
print(price)
