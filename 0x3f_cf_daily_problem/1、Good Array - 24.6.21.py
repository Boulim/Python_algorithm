Good Array
"""
题目链接： Problem - 1077C - Codeforces
思路：（1300）

    好数组的某个数 x = 其余元素的和。
    那么 x 必须是好数组的最大值（如果 x 不是最大值，那么其余元素的和包含最大值，比 x 还要大）
    所以好数组必须满足：最大值 = 好数组的元素和 - 最大值，即最大值 * 2 = 好数组的元素和
    维护 a 的最大值 mx、次大值 mx2、最大值的下标。
    如果删除的不是最大值，那么需要满足 sum(a) - a[i] == mx * 2。
    如果删除的是最大值，那么需要满足 sum(a) - a[i] == mx2 * 2。
"""
Python代码：
n = int(input())
a = [*map(int, input().split())]
s, c = sum(a), sorted(a)
k = []
for i in range(n):
    if(a[i]==c[-1]):
        if(c[-2] == s-c[-1]-c[-2]):#删除的是最大值，所以要使次大值等于除了次大值之外的sum
            k.append(i+1)
    else:
        if(c[-1] == s-c[-1]-a[i]):#删除的不是最大值，删除某个数之后，除了最大值的sum应该等于最大值
            k.append(i+1)
print(len(k))
print(*k)
