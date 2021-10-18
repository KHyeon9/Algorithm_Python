S = int(input())
S2 = int(input())

Over = S2 - S

if S2 > S:
    if 1 <= Over <= 20:
        print("You are speeding and your fine is $100.")

    elif 21 <= Over <= 30:
        print("You are speeding and your fine is $270.")

    else:
        print("You are speeding and your fine is $500.")

else:
    print("Congratulations, you are within the speed limit!")