Avoid K Palindrome
"""
题目链接:https://atcoder.jp/contests/abc359/tasks/abc359_d
判断所有长度为 k 的二进制数中哪些是回文。通过遍历所有可能的二进制数并检查其对称位置的位是否相同来实现的。
如果某个二进制数是回文，则在 pal 数组中标记为 True。

代码使用递归函数 dfs 来处理字符串的每个位置。递归函数的参数 i 表示当前处理的字符串位置，j 表示当前的二进制状态。
对于每个位置 i，代码尝试将其设置为 A 或 B（分别对应二进制的0和1）。如果当前字符是 ?，则可以选择任意值；否则，必须匹配字符 s[i]。
更新二进制状态 j，并检查新的状态是否为回文。如果是，则递归处理下一个位置。

从字符串的最后一个位置开始递归调用 dfs，从字符串的末尾开始，逐步向前计算满足条件的字符串数量。
"""
"""
灵茶思路：
把 AB 信息用二进制压缩表示。
下面的写法中，二进制高位对应的字母在 s 中更靠右的位置，二进制低位对应的字母在 s 中更靠左的位置。

从右往左递归。
定义 dfs(i,j)，其中 i 右边的 k-1 个字母的二进制为 j，计算替换 s[0] 到 s[i] 中的 ?，能得到多少个合法子串。
枚举 b=0,1（如果 s[i]!=? 则 b=s[i]&1）。
把 b 和 j 拼起来，即 t = j<<1 | b，如果 i>n-k，或者得到的二进制数 t 不是回文的，那么就递归到 dfs(i-1, t&mask)，其中 mask = (1 << (k-1)) - 1，用来去掉二进制的最高位。

递归边界：dfs(-1,j)=1，表示找到了一个合法字符串。
递归入口：dfs(n-1,0)。
"""

Python代码:
import sys
from functools import lru_cache
sys.setrecursionlimit(20000)
MOD = 998244353
n, k = map(int, input().split())
s = input()

pal = [False] * (1 << k)    #初始化一个长度为 2^k 的布尔数组 pal，用于标记回文子串。
for i in range(len(pal)):    #遍历所有可能的长度为 k 的二进制数。
    for j in range(k // 2):  #检查每个二进制数是否是回文
        if (i >> j) & 1 != (i >> (k - 1 - j)) & 1:   #如果某个位置的位与其对称位置的位不相同，则不是回文。
            break
    else:
        pal[i] = True  #如果内层循环没有被 break 打断，则该二进制数是回文。
    
mask = (1 << (k - 1)) - 1  #截取二进制数的低 k-1 位。
@lru_cache(None)
def dfs(i, j):
    if i < 0:
        return 1  #如果 i 小于0，返回1。
    res = 0
    for b in range(2):  #遍历二进制的两个可能值（0和1）。
        if s[i] != '?' and s[i] != chr(b + 65):  #如果当前字符不是 ? 且不等于 A 或 B，则跳过。
            continue
        tmp = j << 1 | b  #更新二进制状态
        if i > n - k or not pal[tmp]:  #如果当前状态不是回文或超出范围，则递归调用 dfs
            res += dfs(i - 1, tmp & mask)
    res %= MOD
    return res
print(dfs(n - 1, 0))
