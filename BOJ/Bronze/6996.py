for _ in range(int(input())):
    a, b = input().split()
    s1, s2 = sorted(a), sorted(b)
    if s1 == s2:
        print(f"{a} & {b} are anagrams.")
    else:
        print(f"{a} & {b} are NOT anagrams.")
