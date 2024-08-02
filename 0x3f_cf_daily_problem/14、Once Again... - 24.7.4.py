Once Again...
"""
题目链接:
  Problem - 582B - Codeforces
思路：（1900）（没咋明白）
如果 t <= n，那么直接求长为 tn 的数组的 LIS。也就是对数组 a 循环 t 次。
如果 t > n，只需要循环 n 次。
设最后一轮循环（第 n 轮循环）二分的数组 f 的长度增加了 d，那么有如下结论：
接下来的 t-n 轮循环是不需要跑的，保证每轮循环 f 数组的长度都会增加 d。

例如 a=[2,3,1]，前三轮循环，找到的 LIS 为
[2,3]
[1,2,3]
[1,1,2,3]
后面每轮循环都只会让 f 的长度增加 1。相当于每多一轮循环，中间就插入了一个 1。

"""
Python代码:
import sys
input = lambda:sys.stdin.readline().strip()
from bisect import bisect_right
n, t = map(int, input().split())
a = list(map(int, input().split()))
d = 0
g = []
k = min(t,n)
for _ in range(k):  
    m = len(g)
    for x in a:
        j = bisect_right(g,x)
        if j == len(g):
            g.append(x)
        else:
            g[j] = x
    d = len(g) - m
print(len(g) + (t - k) * d)


