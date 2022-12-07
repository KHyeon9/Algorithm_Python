a, b = input().split()
a_weight = sum(list(map(int, a))) * len(a)
b_weight = sum(list(map(int, b))) * len(b)

if a_weight > b_weight:
    print(1)
elif a_weight < b_weight:
    print(2)
else:
    print(0)
