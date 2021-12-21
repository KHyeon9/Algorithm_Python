n, m = map(int, input().split())
site_password = {}
for _ in range(n):
    site, password = input().split()
    site_password[site] = password
for _ in range(m):
    print(site_password[input()])
