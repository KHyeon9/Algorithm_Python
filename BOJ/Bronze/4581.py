while True:
    vote = input()

    if vote == '#':
        break

    if vote.count("A") >= len(vote) / 2:
        print("need quorum")
    elif vote.count("Y") > vote.count("N"):
        print("yes")
    elif vote.count("Y") < vote.count("N"):
        print("no")
    else:
        print("tie")