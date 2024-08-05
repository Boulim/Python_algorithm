Twist the Permutation
"""
题目链接:
https://codeforces.com/problemset/problem/1650/D
思路：（1300）
给出的是循环移位后的数组，从大到小开始恢复数组。
总共需要n-1次循环。在循环里，找到最大值的当前值坐标，并算出循环移位的次数，
再去掉这个数，将剩余数变回移位前的状态。
"""
Python代码:
import sys
input = lambda:sys.stdin.readline().strip()
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    #给出了修改后的数组，问能不能通过变化，变成顺序数组
    #找到6，找5，找4，找3，找2，先找n，再递减再找
    ans = []
    for i in range(n,0,-1):#从n到1逐个找
        idx = a.index(i)
        ans.append((idx+1) % i)
        a = a[idx+1:] + a[:idx] #一边移位，一边删除元素,就不用再处理多余部分了
    print(*ans[::-1])


