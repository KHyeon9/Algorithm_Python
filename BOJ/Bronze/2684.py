arr = ['TTT', 'TTH', 'THT', 'THH', 'HTT',
       'HTH', 'HHT', 'HHH']
for _ in range(int(input())):
    cnt = {'TTT': 0, 'TTH': 0, 'THT': 0, 'THH': 0,
           'HTT': 0, 'HTH': 0, 'HHT': 0, 'HHH': 0}
    s = input()
    for i in range(38):
        cnt[s[i:i+3]] += 1
    for c in arr:
        print(cnt[c], end=' ')
    print()