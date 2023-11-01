elder = input()
n = int(input())
obey = [elder]

for i in range(n):
    z1, z2 = input().split()

    if z2 == elder:
        elder = z1
        if z1 not in obey:
            obey.append(z1)

print(elder)
print(len(obey))