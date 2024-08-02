Messenger in MAC
"""
题目链接:
  Problem - 1935C - Codeforces
思路：（1800）
遍历数组的每个子集，最小化b的绝对差值，这里对b按照从小到大排序，就可以得到b绝对差值的最小值，这样可以得到对部分a数组的和最大化，最大上限就是L - b的绝对差值和。通过遍历子集，用小根堆存储a的负值，这样每次弹出的都是大的a值，比较每次小根堆之和是否大于最大上限，大于就弹出大的a值。答案就是每次符合条件的小根堆长度的最大值。
"""
Python代码:
import sys
input = lambda:sys.stdin.readline().strip()
from heapq import heappop, heappush
for _ in range(int(input())):
    n, l = map(int, input().split())
    s = []
    for i in range(n):
        a, b = map(int, input().split())
        s.append([b, a])
    s.sort()
    ans = 0
    for i in range(n):
        h = []
        res = 0
        for j in range(i, n):
            heappush(h, -s[j][1])
            res += s[j][1]
            while h and s[j][0] - s[i][0] + res > l:
                res += heappop(h)
            ans = max(ans, len(h))
    print(ans)
