colors = ['black', 'brown', 'red', 'orange', 'yellow', 'green',
          'blue', 'violet', 'grey', 'white']
r = ''
for i in range(3):
    color = input()
    for j in range(10):
        if color == colors[j]:
            if i == 2:
                r = int(r) * (10 ** j)
            else:
                r += str(j)
print(r)
