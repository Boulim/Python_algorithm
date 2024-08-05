Qingshan Loves Strings 2
"""
题目链接:
https://codeforces.com/contest/1889/problem/A
思路：（1300）
当字符串a中的1的个数不等于0的个数，无法构造出符合题意的字符串，返回-1
遍历字符串，当两侧都为0，在右侧加上01串；当两侧都为1，在左侧加上01串。
同时对字符串进行处理。
# 6
# 001110
# 0011100011
# 如果两边都是0 那么在右边+ 01串
# 4
# 1001
# 011001
# 如果两边都是1 在左边+ 01串
"""
Python代码1:
import sys
input = lambda:sys.stdin.readline().strip()
for _ in range(int(input())):
    n = int(input())
    a = list(input())
    if a.count('0') != n / 2:
        print('-1')
        continue
    ans = []
    l, r = 0, n - 1
    while l < r:
        if a[l] != a[r]:
            l += 1
            r -= 1
        elif a[l] == '0':           
            a = a[:r + 1] + ['0', '1'] + a[r + 1:]
            l += 1
            r += 1
            ans.append(r)
        else:
            ans.append(l)
            a = a[:l] + ['0','1'] + a[l:]
            l += 1
            r += 1
    print(len(ans))
    print(*ans)
"""
优化做法：可以用双端队列来维护整个字符串，这样左右插入就会变得很方便，用0，n表示初始插入的位置。
"""
Python代码2:
import sys
input = lambda:sys.stdin.readline().strip()
from collections import deque
for _ in range(int(input())):
    n = int(input())
    a = input()
    if a.count('0') != n / 2:
        print('-1')
        continue
    
    q = deque(a)
    ans = []
    front, rear = 0, n
    while q:
        if q[0] != q[-1]:
            q.pop()
            q.popleft()
            rear -= 2
        elif q[0] == '0':           
            q.append('0')
            q.popleft()
            ans.append(rear)
        else:
            q.appendleft('1')
            q.pop()
            ans.append(front)
        front += 1
        rear += 1
    print(len(ans))
    print(*ans)

