import math

n = int(input())
ans = 0
for i in range(1, int(-(-n**0.5//1))+1):
    if n%i == 0:
        m = n//i - 1
        if i < m: ans += m 
print(ans)