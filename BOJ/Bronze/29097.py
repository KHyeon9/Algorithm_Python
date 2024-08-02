li = list(map(int, input().split()))
res = [li[i] * li[i + 3] for i in range(3)]
names = ["Joffrey", "Robb", "Stannis"]

for i in range(3):
    if max(res) == res[i]:
        print(names[i], end=" ")