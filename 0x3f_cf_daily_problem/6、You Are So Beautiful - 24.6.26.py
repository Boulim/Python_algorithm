You Are So Beautiful
"""
题目链接：
   Problem - F - Codeforces
思路：（1400）
考察子数组最左边和最右边的元素。
条件一：子数组最左边的元素 a[L]，其左侧不能有等于 a[L] 的元素，否则子序列不唯一。
条件二：子数组最右边的元素 a[R]，其右侧不能有等于 a[R] 的元素，否则子序列不唯一。

结论：满足这两个条件，则子序列是唯一的。
证明：用反证法证明。
假设子序列不唯一，那么另一个子序列的不同下标一定位于 [L,R] 内部（如果位于 [L,R] 外面就破坏了条件一或条件二），但是这个范围内的所有下标我们都选了，不可能存在一个子序列没有而另一个子序列有的情况，矛盾，故原命题成立。

怎么计算子数组个数呢？
前后缀分解。
处理出每个 a[i] 首次和最后一次出现的位置。（实际只需要处理最后一次）
枚举 a[i] 作为左端点，那么 a[i] 必须是首次出现的元素，我们还需要知道 >=i 的且是最后一次出现的元素的个数，具体见代码。
"""

Python代码:
import sys
input = lambda:sys.stdin.readline().strip()
from collections import Counter
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)#统计每个数出现几次
    s = set()#存储第一次出现的数都有哪些
    res = 0
    for x in a:
        s.add(x)
        c[x] -= 1
        if c[x] == 0:#如果该数最后一次出现，分别让他与第一次出现的数组队
            res += len(s)#也就是加上第一次出现的集合的大小。
    print(res)

