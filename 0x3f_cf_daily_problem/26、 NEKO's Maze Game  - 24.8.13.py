NEKO's Maze Game
"""
题目链接：https://codeforces.com/problemset/problem/1292/A
思路：（1400）
如果存在两个障碍格，它们上下相邻，或者斜向相邻，那么就无法从起点走到终点。
这启发我们统计这样的障碍格的 pair 个数。

例如 (1,5) 变成障碍格，那么就看 (2,4), (2,5), (2,6) 这三个格子是否为障碍格，若这三个格子中有 x 个障碍格，那么 pair 个数就增加 x。
例如 (1,5) 变成空格子，那么就看 (2,4), (2,5), (2,6) 这三个格子是否为障碍格，若这三个格子中有 x 个障碍格，那么 pair 个数就减少 x。

如果 pair 个数 = 0，那么就可以从起点走到终点，反之不行
"""
# python代码：
import sys
input = lambda:sys.stdin.readline().strip()
n, q = map(int, input().split())
cnt = 0
ban = [[0] * (n + 1) for _ in range(2)]

for _ in range(q):
    r, c = map(int, input().split())
    r -= 1
    c -= 1
    ban[r][c] ^= 1
    s = ban[r ^ 1][c] + ban[r ^ 1][c - 1] + ban[r ^ 1][c + 1]
    
    if ban[r][c] > 0:
        cnt += s
    else:
        cnt -= s
    
    if cnt > 0:
        print("No")
    else:
        print("Yes")
