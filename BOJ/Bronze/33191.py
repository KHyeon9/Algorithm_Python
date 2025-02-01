prices = [int(input()) for _ in range(4)]

my_cost = prices[0]

if my_cost >= prices[1]:
    print("Watermelon")
elif my_cost >= prices[2]:
    print("Pomegranates")
elif my_cost >= prices[3]:
    print("Nuts")
else:
    print("Nothing")

