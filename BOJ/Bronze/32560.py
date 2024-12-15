from collections import Counter # 갯수를 쉽게 세어 딕셔너리 작성

a = input()
b = input()

count = Counter(a) | Counter(b) # 최대 합집합

res = ""

for key, val in count.items():
    res += key * val

print(res)