Vlad and the Mountains
"""
题目链接:
  Problem - G - Codeforces

思路：（2000）
从 a 到 b，路径上的山的高度必须都 <= h[a] + e。

把询问按照 h[a]+e 从小到大排序，有路的山也从小到大排序，为了边查询边建立并查集
遍历询问和 h 数组，对于所有高度 <= h[a]+e 的山 x，用并查集合并。如果 a 和 b 被合并在一起，说明可以从 a 到 b。
"""
Python代码:
import sys
input = lambda:sys.stdin.readline().strip()
def find(x):
    if p[x] != x: p[x] = find(p[x])
    return p[x]
 
def union(a,b):
    a=find(a)
    b=find(b)
    if a!=b: 
        p[a]=b
 
for _ in range(int(input())):
    n,m=map(int,input().split())
    h=[0] + list(map(int,input().split()))
 
    edges=[]
    for _ in range(m):
        a,b=map(int,input().split())
        edges.append([max(h[a],h[b]),a,b])
        #记录一条路，以及两座山的最高值，之后需要判断h + e>= max，能就能上。
        #按照山峰最大值从小到大排序
    q=int(input())
    queries=[]
    for i in range(q):
        a,b,e=map(int,input().split())
        queries.append([h[a]+e,a,b,i])
    #将询问按照h+e排序。在从小到大处理询问的时候，正好也是建立并查集的时候
    #同时记录查询的顺序，方便打印答案
    edges.sort()
    queries.sort()
 
    cnt=0 #表示经过了几座山
    p=[i for i in range(n+1)]
    ans=[]
    for i in range(q):
        #当前走到第cnt个山，而且当前体力h+e可以走第cnt个山
        #处理小部分并查集，满足条件的路上的两座山放入并查集
        while cnt < m and edges[cnt][0]<=queries[i][0]:
            a,b = edges[cnt][1],edges[cnt][2]
            pa,pb = find(a),find(b)
            if pa!=pb: 
                p[pa] = pb 
            cnt+=1
        
        #如果a，b两山在一个并查集，就能到达。
        if find(queries[i][1])==find(queries[i][2]):
            ans.append([queries[i][3],1])
        else:
            ans.append([queries[i][3],0])
 
    ans.sort()#按照询问的编号排序
    for x in ans:
        if x[1]: print("YES")
        else: print("NO")
    print()

