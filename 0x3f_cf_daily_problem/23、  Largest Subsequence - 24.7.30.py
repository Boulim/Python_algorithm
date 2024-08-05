Largest Subsequence
"""
题目链接：
https://codeforces.com/contest/1905/submission/273453464
思路：（1400）
字典序最大子序列可以用单调栈求出。
由于字典序最大子序列是递减的，把子序列反转，如果 s 不是有序的，输出 -1。
否则，例如 bbbaa 循环右移 2 次就变成 aabbb 有序的了，所以答案为去掉和子序列首字母一样的字母后，
子序列的剩余字母个数。
"""

Python代码:
import sys
input = lambda:sys.stdin.readline().strip()


for _ in range(int(input())):
    n = int(input())
    s = list(input())

    st = []
    for i, x in enumerate(s):
        while st and s[st[-1]] < x: st.pop()
        st += [i]

    t = s[:]
    for i in range(len(st)>>1):
        t[st[i]], t[st[-i-1]] = t[st[-i-1]], t[st[i]]

    if t == sorted(t):
        i = 0
        while i < len(st) and s[st[i]] == s[st[0]]: i += 1
        print(len(st)-i)
    else:
        print(-1)
