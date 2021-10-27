n, w, h, l = map(int, input().split())

r = (w // l) * (h // l)

if n >= r:
    print(r)
    
else:
    print(n)