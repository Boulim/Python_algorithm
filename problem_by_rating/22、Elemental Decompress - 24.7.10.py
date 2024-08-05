Elemental Decompress
"""
题目链接：https://codeforces.com/problemset/problem/1768/C
思路：（1300）
统计每个数字出现的下标，如果当前数字出现了两次，将值分别记录到p和q中两个不同下标中，再把下标记录到q和p的下标记录器中。
如果只出现一次，把当前值都给p和q。如果当前数字一次都没出现，就分配到数字出现两次的下标中。如果没有出现两次的，就不存在这样的数组
为了保证最大值，应该从大到小遍历。
"""
Python代码:
import sys
input = lambda:sys.stdin.readline().strip()
for _ in range(int(input())):
    yes = True
    n = int(input())
    a = list(map(int, input().split()))
    p, q = [0] * n, [0] * n
    pos = [[] for i in range(n + 1)]
    for i in range(n):  #存储每个值出现的次数
        pos[a[i]].append(i)
    rp, rq = [], []
    for i in range(n, 0, -1): #从数值从大到小
        if len(pos[i]) == 2:
            p[pos[i][0]] = i #第一次出现的值给q
            q[pos[i][1]] = i #第二次出现的值给p
            rq.append(pos[i][0]) #在q里记录p下标
            rp.append(pos[i][1]) #在p里记录q下标
            continue
        if len(pos[i]) == 1: #只出现一次
            p[pos[i][0]] = i #那么p和q的位置只能放这个数
            q[pos[i][0]] = i
            continue
        if len(rp) > 0 and len(rq) > 0:#没出现的数字，分到出现两次的对应坐标下。
            p[rp.pop()] = i
            q[rq.pop()] = i
        else:    #没出现的数字无处安放
            yes = False
    if yes:
        print("YES")
        print(*p)
        print(*q)
    else:
        print("NO")


