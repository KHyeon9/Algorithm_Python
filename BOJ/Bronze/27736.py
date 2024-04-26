n = int(input())
vote = list(map(int, input().split()))

if vote.count(0) >= n / 2:
    print("INVALID")
elif vote.count(-1) >= vote.count(1):
    print("REJECTED")
else:
    print("APPROVED")