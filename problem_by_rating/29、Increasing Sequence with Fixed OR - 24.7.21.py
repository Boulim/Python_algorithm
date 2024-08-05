Increasing Sequence with Fixed OR
"""
题目链接:
https://codeforces.com/contest/1988/problem/C
位运算，求递增数组，使相邻两项或为n。
可以从最高位的1开始舍去，第一个数舍弃最高位的1，第二个数舍去次高位的1，第三个数舍去第三高位的1，这样每次或值一定为n，且是从小到大排序的。
2 ^ 60 > 10 ^ 18
    14  1110   
  = 6    110   从高到低, 依次减去第i高位的1，结果就是答案
    10  1010
    12  1100
    14  1110
"""
Python代码:
import sys
input = lambda:sys.stdin.readline().strip()
for _ in range(int(input())):
    n = int(input())
    ans = []
    for i in range(59, -1, -1):
        x = 1 << i
        if (x & n) == x and x != n:
            ans.append(n - x)
    ans.append(n)
    print(len(ans))
    print(*ans)



