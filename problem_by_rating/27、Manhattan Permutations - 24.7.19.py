Manhattan Permutations
"""
题目链接:
https://codeforces.com/problemset/problem/1978/C
思路：（1300）
通过观察可以看到，k为奇数一定返回no，k大于逆序得到的曼哈顿值时，也返回no
当k为偶数，定义a为1-n的一个数组，可以通过双指针，因为曼哈顿值从中间化成了相等的两份，可以先比较k是否大于i- j的二倍，如果可以就减去，交换a的两个值，同时移动指针，不行就只移动一侧的指针。
如果最后k为1，代表k为奇数，或者k大于1，代表k大于最大的曼哈顿值，都返回no
剩下的返回yes，并打印a
"""
Python代码:
import sys
input = lambda: sys.stdin.readline().strip()
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = [i + 1 for i in range(n)]
    i, j = 0, n - 1
    while i < j:
        if k >= 2 * (j - i):
            k -= 2 * (j - i)
            a[i], a[j] = a[j], a[i]
            j -= 1
        i += 1
    if k:
        print("No")
    else:
        print("Yes")
        print(*a)
