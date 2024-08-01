Kolya and Movie Theatre
"""
题目链接:
  Problem - 1862E - Codeforces
思路：（1600）

看电影的消耗始终等于最后一天的cnt* d，也就是（i+1） * d。那么只需要关注选哪m个电影才能让总娱乐价值最大。
遍历数组，同时维护一个堆，堆内放遍历时前m大的元素，那么堆内元素和 - （i+1）* d 就是结果，只需选择每次堆内结果的最大值就可。
"""
Python代码:
import sys
input = lambda:sys.stdin.readline().strip()
from heapq import heappop, heappush
for _ in range(int(input())):
    n, m, d = map(int, input().split())
    a = list(map(int,input().split()))
    h =[]
    ans = 0
    s = 0
    for i in range(n):
        if a[i] <= 0 :
            continue
        s += a[i]
        heappush(h,a[i])
        if len(h) > m:
            s -= heappop(h)
        ans = max(ans, s - d * (i + 1))
    print(ans)
        


