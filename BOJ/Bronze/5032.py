e, f, c = map(int, input().split())
new_drink = 0
bottle = e + f

while bottle >= c:
    new_drink += bottle // c
    bottle = bottle // c + bottle % c

print(new_drink)

