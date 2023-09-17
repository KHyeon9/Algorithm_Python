s = input()
arr, res = "aeiou", ""

for w in s:
    if w in arr:
        res += w

print("S" if res == res[::-1] else "N")