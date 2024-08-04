Ice Cream Balls
"""
题目链接:https://codeforces.com/contest/1862/problem/D
思路：（1300）
要制作恰好n个种类的冰淇淋，需要先制作冰淇淋球不同的冰淇淋m= (1 + isqrt(1 + 8 * n)) //2 个（求根公式），剩下n - m(m - 1)/2 个用相同口味的冰淇淋球做。
因为若再加一个不同口味，则会超过n个，不符合恰好。而每个冰淇淋要制作相同口味，只需要再加1个就好。
"""
Python代码:
import sys
input = lambda:sys.stdin.readline().strip()
from math import isqrt
for _ in range(int(input())):
    n = int(input())
    m = (1 + isqrt(1 + 8 * n)) //2 
    print(n + m - (m - 1) * m // 2)#正好数量为n

