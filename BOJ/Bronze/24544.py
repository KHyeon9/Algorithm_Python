n = int(input())
interest = list(map(int, input().split()))
registration = list(map(int, input().split()))
not_regust = 0

for i in range(n):
    if registration[i] == 0:
        not_regust += interest[i]
print(sum(interest))
print(not_regust)
