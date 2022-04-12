agent_name = [input() for _ in range(5)]
result = []
for i in range(5):
    if "FBI" in agent_name[i]:
        result.append(i + 1)

if len(result) == 0:
    print("HE GOT AWAY!")
else:
    print(*result)