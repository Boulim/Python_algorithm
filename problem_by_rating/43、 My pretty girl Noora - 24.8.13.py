My pretty girl Noora
"""
题目链接：https://codeforces.com/contest/822/problem/D
思路：（1800）
为了让次数最小化，每次分队伍时，应该把总人数的最小质数当作队伍人数。

每局的次数都可以递归到规模更小的局的次数， 可以用 dp 。

倒序按照秦久韶算法依次来算。
"""
#python代码：
import sys
input = lambda:sys.stdin.readline().strip()
t, l, r = map(int, input().split())
n = 5 * 10 ** 6
st = [False] * (n + 1)  
p = [0] * (n + 1)  
dp = [0] * (n  + 1)
mod = 10 ** 9 + 7
for i in range(2, n + 1):
    if st[i] == False: 
        p[i] = i
    
    for j in range(i * i, n + 1, i):
        st[j] = True  
        if p[j] == 0:
            p[j] = i

for i in range(2, n + 1):
    x = p[i]
    dp[i] = (dp[i // x] + i * (x - 1) // 2)

res = 0
for i in range(r, l - 1, -1):
    res = (res * t + dp[i]) % mod
print(res)
