encryption = {}

for i in range(1, 53):
    if i <= 26:
        alpa = chr(ord("a") + i - 1)
        encryption[alpa] = str(i).zfill(2)
    else:
        alpa = chr(ord("A") + i - 27)
        encryption[alpa] = str(i)
line = input()

res = ""

for word in line:
    if word.isdigit():
        res += "#" + word
    elif word.isalpha():
        res += encryption[word]
    else:
        res += word

print(res)
