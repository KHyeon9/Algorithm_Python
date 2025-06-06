k, l = map(int, input().split())
s = input()

alpa_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpa_lower = alpa_upper.lower()
res = ""

for ch in s:
    # 소문자인 경우
    if ch.islower():
        idx = (alpa_lower.index(ch) + k) % 26
        res += alpa_lower[idx]
    # 대문자인 경우
    elif ch.isupper():
        idx = (alpa_upper.index(ch) + k) % 26
        res += alpa_upper[idx]
    # 알파벳이 아닌 경우
    else:
        res += ch
print(res)