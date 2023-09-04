for _ in range(int(input())):
    names = list(input().split())
    name = input().strip()
    count = int(input())
    name_index = names.index(name)
    point = (count + name_index - 1) % len(names)

    print(names[point])



