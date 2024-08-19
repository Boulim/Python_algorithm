"""
题目链接：https://codeforces.com/contest/578/problem/A
思路：如果 a ,b 两点在函数图像上， 让这段图像平移到坐标轴原点， 两点变为 a', b。

当处于上升阶段， 有 a' = b,图像过点(a' - b, 0), 当处于下降阶段，图像过点(a' + b, 0)。 分到周期的起点（或者称之为终点）。 以下简称这两个横坐标为 c。

那么 c 必定为 周期 2 * x 的整数倍。 假设这个整数为 n 。则 n = c // (2 * x) ,  转化一下，  x = c // (2 * n)

又有 x >= b , 有 c // (2 * n ) >= b. 即 n  <= c // (2 * b), x >= c // (2 * ( c //(2 * b))

x 取最小值且为浮点数， 有 x = c / (2 * ( c // (2 * b)).
"""
#python 代码：
import sys
input = lambda:sys.stdin.readline().strip()

a, b = map(int, input().split())
if b > a:
    print('-1')
else:
    print((a + b) / (2 * ((a + b) // (2 * b))))
