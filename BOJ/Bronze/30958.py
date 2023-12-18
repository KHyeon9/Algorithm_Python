n = int(input())
logo_song = input()
res = 0

for w in "abcdefghijklmnopqrstuvwxyz":
    res = max(logo_song.count(w), res)

print(res)