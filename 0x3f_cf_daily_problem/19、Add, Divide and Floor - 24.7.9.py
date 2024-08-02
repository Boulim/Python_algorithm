Add, Divide and Floor
"""
题目链接:
19、 Problem - 1901C - Codeforces
思路：（1400）
将数组都+x并整除2后变成数组每个数都相同。考虑每次都加最小值并除以2，最终变为整个数组只有最小值。再进一步想，只要把最大值变成和最小值相等，那么数组中其他数自然会和最小值相等。
"""
Python代码:

import sys
input = lambda:sys.stdin.readline().strip()
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    # """
    # 用一个x对整个数组操作一遍, 这算一次.
    # 现在先考虑x是怎么来的
    # 每次都会+x整除2。
    # 每次加最小值， 那就只需要判断最大值就好了
    # """
    cnt = 0
    a.sort()
    while a[0] != a[-1]:
        a[-1] = (a[-1] + a[0]) // 2
        cnt += 1
    print(cnt)
    if cnt <= n:
        print(*[a[0]] * cnt)

