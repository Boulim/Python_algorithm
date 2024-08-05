Divisor Chain
"""
题目链接:https://codeforces.com/problemset/problem/1864/C
思路：（1300）
依次去掉x二进制中为1的位置，用x&-x提取最后一个1，用x&(x - 1)判断是否只剩下一个1，
如果不是，就去掉多余的1，如果只剩1个1，就直接右移除以2，去掉这个1.
"""
Python代码:
import sys
input = lambda:sys.stdin.readline().strip()
for _ in range(int(input())):
    x = int(input())
    ans = []
    while x:
        ans += [x]
        if x & (x - 1): #去掉二进制串的最后一个1之后，还大于0
            x -= x & -x #减去二进制串的最后一个1，也就是1+后边的一串0
#x -= x & -x 也可以写为x & (x - 1)
        else:
            x >>= 1 #剩下类似于10000的串，除以2，二进制右移。
    print(len(ans))
    print(*ans)
        

