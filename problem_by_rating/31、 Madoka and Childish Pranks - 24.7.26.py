Madoka and Childish Pranks
"""
题目链接:
https://codeforces.com/contest/1647/problem/C
思路：（1300）
当左上角第一个为黑色，怎么也构造不出，所以返回-1
将棋局划分成更小的格子，分别是横着的白黑，和竖着的白黑。这样一个大棋局被分成了两个特殊的小部分。考虑从最后一行的最后一个倒着处理。如果不是在第一列，就加上横着的，在第一列加上竖着的。
从最后一排开始铺，遇到左边界为黑色 竖直铺，第一行第一个不能为黑色
"""
Python代码:
import sys
input = lambda:sys.stdin.readline().strip()
for _ in range(int(input())):
    n, m = map(int, input().split())
    g = [list(input()) for _ in range(n)]
    if g[0][0] == '1':
        print('-1')
        continue
    ans = []
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if g[i][j] == '1' and j:
                ans.append([i + 1, j, i + 1, j + 1])
            elif g[i][j] == '1' and j == 0:
                ans.append([i, j + 1, i + 1, j + 1])
    print(len(ans))
    for x in ans:
        print(*x)

