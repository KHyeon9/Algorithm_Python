N = int(input())
lines = [input()for _ in range(N)]

promise = [
    'Never gonna give you up',
    'Never gonna let you down',
    'Never gonna run around and desert you',
    'Never gonna make you cry',
    'Never gonna say goodbye',
    'Never gonna tell a lie and hurt you',
    'Never gonna stop',
]

for l in lines:
    if l not in promise:
        print('Yes')
        exit()

print('No')