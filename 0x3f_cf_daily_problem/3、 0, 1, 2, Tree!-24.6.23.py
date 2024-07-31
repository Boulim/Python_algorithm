0, 1, 2, Tree!
"""
题目链接：
  Problem - 1950F - Codeforces
思路：（1700）
把这三种节点（有两个/一个/零个儿子）分别记作 A B C。一层一层地放置，先放 A，然后 B，最后 C。

先判断 -1。
由于 a 个节点 A 会产生 a+1 个「插座」，可以插入恰好 a+1 个节点，所以必须满足 a+1=c。
B 节点由于插入插座后自己又产生了一个插座，所以无需判断 b。

对于节点 A 来说，一层一层地放置，可以放 a 的二进制长度层，设其为 h1。(很神奇，二进制长度)
最后一层可以放恰好 c 个节点，还留有 k = 2^h1 - c 个「插座」，可以放一部分节点 B。
如果 b-k > 0，那么剩下的 b-k 个节点需要 h2 = ceil((b-k)/c) 层。也就是(b - k + c - 1=b - k + a)//c 层
最后一层放节点 C。

所以树高为 h1 + h2 + 1 - 1 = h1 + h2，减一是因为按照题目规定，高度等于层数减一。
""""
Python代码：
import sys
input = lambda:sys.stdin.readline().strip()
n  = int(input())
for _ in range(n):
    a,b,c = map(int,input().split())
    if a + 1 != c:
        print(-1)
        continue
    h1 = a.bit_length()#求a二进制长度的函数
    k = 2 ** h1 - c
    if b > k:
        h2 = (b - k + a) // c
        h1 += h2
    print(h1)


