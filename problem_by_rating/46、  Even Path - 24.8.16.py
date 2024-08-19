"""
题目链接：https://codeforces.com/contest/1252/problem/C

思路：将行和列的连续相等的置为相同的数，这样查询的时候可以直接得出答案
"""
# python代码：
n, q = map(int, input().split())
r = list(map(int, input().split()))
c = list(map(int, input().split()))

r1 = list(i for i in range(n))
c1 = list(i for i in range(n))
for i in range(1,n):
    if r[i - 1] % 2 == r[i] % 2:
        r1[i] = r1[i - 1]
    if c[i - 1] % 2 == c[i] % 2:
        c1[i] = c1[i - 1]

for _ in range(q):
    ra, ca, rb, cb =  map(lambda x: int(x) - 1, input().split())
    if r1[ra] == r1[rb] and c1[ca] == c1[cb]:
        print('YES')
    else:
        print("NO")
