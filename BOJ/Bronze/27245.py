w = int(input())
l = int(input())
h = int(input())

if h * 2 <= min(w, l) and min(w, l) * 2 >= max(w, l):
    print("good")
else:
    print("bad")