Nested Segments
"""
题目链接：
  Problem - 976C - Codeforces
思路：（1500）
把区间按照左端点从小到大排序，左端点相同的，按照右端点从大到小排序。排序后，遍历区间。
对于区间 i，如果区间 i 被区间 j 包含，那么区间 j 一定是我们之前遍历过的区间（因为左端点从小到大排序了）。
所以只要区间 j 的右端点 >= 区间 i 的右端点，那么区间 j 就可以包含区间 i。
"""
Python代码:
import sys
input = lambda:sys.stdin.readline().strip()
n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())) + [i])
a.sort(key = lambda f:(f[0], -f[1]))#排序
for i in range(n - 1):
    if a[i][1] >= a[i + 1][1]:#左边的右端>=右边的右端，包含了。
        print(a[i + 1][2] + 1, a[i][2] + 1)
        break
else:
    print(-1, -1)
