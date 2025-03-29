h_s, h_e = map(int, input().split())
s_s, s_e = map(int, input().split())
v_s, v_e = map(int, input().split())
r, g, b = map(int, input().split())

M = max(r, g, b)
m = min(r, g, b)
V = M

S = 255 * ((V - m) / V)

if V == r:
    val1 = 0
    val2 = g - b
elif V == g:
    val1 = 120
    val2 = b - r
else:
    val1 = 240
    val2 = r - g

H = val1 + (60 * val2) / (V - m)

if H < 0:
    H += 360

if h_s <= H <= h_e and s_s <= S <= s_e and v_s <= V <= v_e:
    print("Lumi will like it.")
else:
    print("Lumi will not like it.")
