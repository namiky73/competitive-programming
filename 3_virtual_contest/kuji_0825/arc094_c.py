n = int(input())
INF = 10**9
csum = 0
min_b = INF
for _ in range(n):
    a,b = map(int, input().split())
    csum += a
    if a > b: min_b = min(min_b,b)

if min_b == INF: print(0)
else: print(csum-min_b)

