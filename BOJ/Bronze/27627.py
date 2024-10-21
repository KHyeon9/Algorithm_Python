line = input()

for i in range(1, len(line)):
    s1, s2 = line[:i], line[i:]

    if s1 == s1[::-1] and s2 == s2[::-1]:
        print(s1, s2)
        exit()

print("NO")