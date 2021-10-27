K, D, A = map(int, input().split('/'))

S = K + A

if S < D or D == 0:
    print("hasu")

else:
    print("gosu")