Omkar and Last Class of Math
"""
题目链接:
   Problem - 1372B - Codeforces
思路：（1300）

假设两个数分别为 k , n - k 且 k < n - k。那么肯定有n可以整除k。假设 k * m = n，那么 n - k = k * m  - k  = (m - 1) * k，也是 k 的倍数。故lcm(k, n - k) = n - k。
要使n - k 尽量小，那么k应当尽量大， 即 k 是 n 除了本身之外的最大因数，只需找到除了1之外的最小因数，就可以找到 k 。
设 d 是 n 的最小的 >= 2 的因子，那么 k = n // d，n - k = n - n // d。特别地，如果 n 是质数，那么 k = 1, n - k  = n - 1。
"""
Python代码:
import sys
input = lambda:sys.stdin.readline().strip()
for _ in range(int(input())):
    n = int(input())
    ans = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            ans = n // i
            break
    print(ans, n - ans)

