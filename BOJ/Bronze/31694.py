algosia = list(map(int, input().split()))
bajtek = list(map(int, input().split()))

if sum(algosia) != sum(bajtek):
    print("Algosia" if sum(algosia) > sum(bajtek) else "Bajtek")
    exit()

tie = False

for i in range(10, 0, -1):
    if algosia.count(i) > bajtek.count(i):
        print("Algosia")
        tie = True
        break
    elif algosia.count(i) < bajtek.count(i):
        print("Bajtek")
        tie = True
        break

if not tie:
    print("remis")
