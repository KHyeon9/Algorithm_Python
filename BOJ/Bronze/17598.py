vote = 0
for _ in range(9):
    s = input()
    if s == "Tiger":
        vote += 1

print("Tiger" if vote >= 5 else "Lion")
