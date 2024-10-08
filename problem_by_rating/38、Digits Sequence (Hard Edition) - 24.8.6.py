Digits Sequence (Hard Edition)
"""
题目链接:https://codeforces.com/problemset/problem/1177/B
思路：（1800）
1位数   1 - 9       9 个数    占了9个位置
2位数   10 - 99     90个数    占了90 * 2 = 180个位置
3位数   100 - 999   900个数   占了900 * 3 = 2700个位置
逐渐缩小范围找
1、先找出k位置所在数字x属于几位数, 减去前边位数的个数, 将k变为该位数的次序
2、除以该位数的长度, 找到k是该位数属于第几个数的位置, 将k变为数字x的次序
3、还原k所在的数字x, 从数字x中找到k的位置。
"""
Python代码:
import sys
input = lambda:sys.stdin.readline().strip()

k = int(input()) - 1
base = 1    # 几位数
cnt = 9     # 位置占了多少
start = 1   # base进制开始的第一个的数字
while k > base * cnt:
    k -= base* cnt
    cnt *= 10
    base += 1
    start *= 10

x, y = divmod(k, base)
print(str(x + start)[y])
