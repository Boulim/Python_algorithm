New Year's Eve
"""
题目链接:
https://codeforces.com/contest/912/problem/B
生成一个与 n 的二进制位数相同的全1二进制数。
bin返回0b开头的二进制数，-2就去掉0b，表示二进制实际位数。
"""
Python代码:
n, m = map(int, input().split())
if m == 1:
    print(n)
else:
    print(2 ** (len(bin(n)) - 2) - 1)
