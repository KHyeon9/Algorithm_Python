pibo = [1, 1]

for _ in range(2, 46):
    pibo.append(pibo[-2] + pibo[-1])

for _ in range(int(input())):
    n = int(input())
    print(pibo[n])