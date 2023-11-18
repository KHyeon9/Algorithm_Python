dic  = {
    "S": [],
    "B": [],
    "V": [],
    "K": []
}

for _ in range(51):
    word, num = input().split()
    dic[word].append(int(num))

for word in dic:
    for n in range(1, 14):
        if n not in dic[word]:
            print(word, n)
            exit()
