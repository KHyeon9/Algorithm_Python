s = input().upper()
alpa = [chr(i) for i in range(ord('A'), ord('A') + 26)]

for a in alpa:
    print(f"{a} | " + "*" * s.count(a))
