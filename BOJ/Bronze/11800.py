dic = {1: "Yakk", 2: "Doh", 3: "Seh",
       4: "Ghar", 5: "Bang", 6: "Sheesh"}
dic2 = {1: "Habb Yakk", 2: "Dobara", 3: "Dousa",
        4: "Dorgy", 5: "Dabash", 6: "Dosh"}
for i in range(int(input())):
    a, b = map(int, input().split())
    if a == 6 and b == 5 or a == 5 and b == 6:
        print(f"Case {i + 1}: Sheesh Beesh")
    elif a == b:
        print(f"Case {i + 1}: {dic2[a]}")
    else:
        print(f"Case {i + 1}: {dic[max(a, b)]} {dic[min(a, b)]}")


