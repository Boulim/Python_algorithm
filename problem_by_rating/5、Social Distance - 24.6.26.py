Social Distance
"""
题目链接:https://codeforces.com/problemset/problem/1367/C
5、 Problem - 1367C - Codeforces
思路：（1300）
将字符串前边和后边分别加上k个0，构成一个2k+ 1的判断串。按照1为界限将串分开。
因为存在某个答案，后k个0是下一个答案的前k个0，此时共享k个0。处理时先去掉这k个0，再将剩余长度整除k+1，就可得到当前串的答案，将其加入总答案里。
"""
Python代码1:
import sys
input = lambda:sys.stdin.readline().strip()
for _ in range(int(input())):
    n, k = map(int,input().split())
    res = 0
    for c in ('0' * k +  str(input()) + '0' * k).split('1'):#划分为2k + 1个，每段只处理前边k个0
        res += (len(c) - k) // (k + 1)
    print(res)
"""
暴力版，判断是否存在2 * k + 1个连续0的字串
"""
Python代码2:
import sys
input = lambda:sys.stdin.readline().strip()
for _ in range(int(input())):
    n, k = map(int,input().split())
    t = '0' * k
    s = t +  str(input()) + t#出现连续2 * k 个0，res 才能加1
    c = 0
    res = 0
    for i in range(n + k * 2):
        if s[i] == '1':
            c = 0
        else:
            c += 1
        if c == 2 * k + 1:
            c = k
            res += 1
    print(res)

