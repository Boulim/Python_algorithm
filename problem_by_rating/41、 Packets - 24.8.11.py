Packets
"""
题目链接：https://codeforces.com/problemset/problem/1037/A
思路：（1300）
只要把硬币分为1、 2、 4、 8...等2的次幂，就可以表示任何数， 因此可以直接求大于 n 的 2 的次幂为多少， 打印这个次幂就可以。

用python的bit_length() 直接求二进制长度，就是答案。
"""
Python代码:
print(int(input()).bit_length())
