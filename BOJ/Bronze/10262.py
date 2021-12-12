a = list(map(int, input().split()))
b = list(map(int, input().split()))

if sum(a) > sum(b):
    print("Gunnar")
elif sum(a) < sum(b):
    print("Emma")
else:
    print("Tie")