arr = []

while True:
    line = input()
    if line == "000-00-0000":
        break
    arr.append(line)

for el in sorted(list(set(arr))):
    if arr.count(el) > 1:
        print(el)