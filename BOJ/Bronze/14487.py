n = int(input())
villages = list(map(int, input().split()))
print(sum(villages) - max(villages))