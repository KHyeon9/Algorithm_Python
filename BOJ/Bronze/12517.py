vowel = ['a', 'e', 'i', 'o', 'u']

for i in range(1, int(input()) + 1):
    name = input()

    if name[-1] == 'y':
        print(f"Case #{i}: {name} is ruled by nobody.")
    elif name[-1] in vowel:
        print(f"Case #{i}: {name} is ruled by a queen.")
    else:
        print(f"Case #{i}: {name} is ruled by a king.")