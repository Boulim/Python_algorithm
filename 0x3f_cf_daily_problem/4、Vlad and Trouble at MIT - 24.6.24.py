Vlad and Trouble at MIT
"""
题目链接:
  Problem - G - Codeforces
思路：（1900）
S 只能和 S 连通，不能和 P 连通；P 只能和 P 连通，不能和 S 连通。
假设 0 是树的根。
 f[x][0] 表示以 x 为根的子树，要使 x 和子树中的 S 连通（相当于和 P 不连通），最少需要切断的边数。如果 s[x]=P，则 f[x][0] = inf。
 f[x][1] 表示以 x 为根的子树，要使 x 和子树中的 P 连通（相当于和 S 不连通），最少需要切断的边数。如果 s[x]=S，则 f[x][1] = inf。
遍历 x 的儿子 y，如果 x 要和 S 连通，那么分类讨论：
    如果 y 也和 S 连通，则 f[x][0] += f[y][0]。
    如果 y 和 P 连通，则 f[x][0] += f[y][1] + 1，因为需要断开 x 和 y 之间的边。
二者取最小值，得 f[x][0] += min(f[y][0], f[y][1] + 1)。
同理得f[x][1] += min(f[y][1], f[y][0] + 1)。
代码实现时，无需建树，直接从 i=n 开始倒着遍历，转移到其父节点 a[i] 上。
答案为 min(f[0][0], f[0][1])。
"""
Python代码:
import sys
input = lambda:sys.stdin.readline().strip()
from math import inf
for _ in range(int(input())):
    n = int(input())
    p = [0,0] + list(map(int,input().split()))#补父节点，表示父节点的编号
    s = "#" +input()#补出来一个0号结点
    f = [[0]*2 for _ in range(n+1)]
    for i in range(n, 0, -1):
        if s[i] == 'P': f[i][0] = inf
        if s[i] == 'S': f[i][1] = inf
        f[p[i]][0] += min(f[i][0], f[i][1] + 1)
        f[p[i]][1] += min(f[i][1], f[i][0] + 1)
    print(min(f[0][0],f[0][1]))

