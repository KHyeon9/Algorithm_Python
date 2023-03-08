s = input()
arr = set(list(s))
odd, even = False, False

for i in arr:
    if s.count(i) % 2 == 0:
        even = True
    else:
        odd = True

    if even == odd == True:
        break

if odd == even:
    print(2)

elif odd:
    print(1)
else:
    print(0)