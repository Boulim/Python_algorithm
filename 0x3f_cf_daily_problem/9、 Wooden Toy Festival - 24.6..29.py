Wooden Toy Festival
"""
题目链接：
   Problem - 1840D - Codeforces
思路：（1400）
将数组先排序，再划分成三段，分别由三个工匠做。要求 min|x-y|，那么要尽量让每个工匠都靠近自己段的中心。所以可以考虑列举每个工匠的半径m，找到最小的满足条件的m即可。第一段是[a[0], a[0] + 2 * m]，第二段[a[0] + 2 * m + 1, a[0] + 4 * m + 1]，第三段[a[0] + 4 * m + 2, a[0] + 6 * m + 2]
每段是2 * m，所以数组总长应该满足 6 * m + 2 + a[0] >=a[-1]。有m = (a[-1] - a[0] - 2)/6上取整，也就是 m = (a[-1] - a[0]  + 3)/6。这是半径m的上界。通过二分找到答案。
这里判断第三段长度k,是否为0，或者小于2 * m,是则成立。
"""
Python代码:
import sys
input = lambda:sys.stdin.readline().strip()
import bisect
#bisect.bisect_right返回大于x的第一个下标
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    def check(nums, m):
        l = bisect.bisect_right(nums, nums[0] + 2*m)
        r = bisect.bisect_right(nums, nums[l] + 2*m)
        return r == n or nums[-1] - nums[r] <= 2*m
    l, r = 0, (a[-1] - a[0] + 3) // 6
    while l < r:
        m = (l + r) // 2
        if check(a, m):
            r = m
        else:
            l = m + 1
    print(r)

