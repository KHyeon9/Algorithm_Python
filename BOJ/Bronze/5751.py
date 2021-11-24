while 1:
    t = int(input())
    m = 0
    j = 0
    
    if t == 0:
        break
        
    n = list(map(int, input().split()))
    
    for i in range(t):
        if n[i] == 0:
            m += 1
        else:
            j += 1
    print("Mary won {} times and John won {} times".format(m, j))