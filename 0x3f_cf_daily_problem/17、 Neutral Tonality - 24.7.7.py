Neutral Tonality
"""
题目链接:
17、 Problem - 1893B - Codeforces
思路：（1700）
从特殊到一般，思考如下情况：a 单调递减。a 单调递增。
min(a) = a[0]min(a) ≠ a[0]
构造方法：
先把 b 从大到小排序。然后双指针遍历 a 和 b 合并成 c，在把 a[i] 加到 c 之前，必须把 >= a[i] 的 b[j] 都加到 c。
"""
Python代码:
import sys
input = lambda:sys.stdin.readline().strip()
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = sorted(list(map(int, input().split())))#从小到大排序
    c = []
    for x in a:
        while b and b[-1] >= x:
            c.append(b.pop())
        c.append(x)
    c.extend(b[::-1])#逆序从大到小插入
    print(*c)


