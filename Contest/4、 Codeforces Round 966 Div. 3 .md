# [Codeforces Round 966 Div. 3](https://codeforces.com/contest/2000)
- 每道题目的链接在文末

- Date：2024.08.14

- 排名 1w4 ，c题被卡了， 呜呜呜！
         
---
> [A、Primary Task](https://codeforces.com/contest/2000/problem/A)

**思路:** 暴力判断题， 只需要枚举每种不满足的情况就可以。   

当数字串长度 `<= 2`， 或者 前两个字符不是 `10`，或者第三个数字是 `0`， 或者长度等于3， 但是第三个是 `1` 或者 `0` 。

当不满足以上条件时，输出 `YES`。

`Python代码：`
```Python []
import sys
input = lambda:sys.stdin.readline().strip()

for _ in range(int(input())):
    a = str(input())
    n = len(a)
    if n <= 2 or a[:2] != '10' or (n == 3 and int(a[2]) < 2) or (n > 3 and a[2] == '0'):
        print("NO")
    else:
        print("YES")
```
<br></br>

> [B、Seating in a Bus](https://codeforces.com/contest/2000/problem/B)

**思路:** 要求坐座位连续， 那么可以初始第一个人的位置。 用双指针来解答。 

当第二个人在第一个人左边， 让 l -= 1 ， 在第一个人右边， 让 r += 1 。

如果不满足在已有的人的左边或者右边， 输出 `NO` 。

`Python代码：`
```Python []
import sys
input = lambda:sys.stdin.readline().strip()

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    l, r = a[0], a[0]
    st = True
    for i in range(1, n):
        if a[i] == l - 1:
            l -= 1
        elif a[i] == r + 1:
            r += 1
        else:
            st = False
            break
    if st:
        print("YES")
    else:
        print("NO")
```
<br></br>

> [C、Numeric String Template](https://codeforces.com/contest/2000/problem/C)

**思路:** 哈希会有冲突，被卡掉了。 换一种做法， 每次扫描数组的时候， 判断。

遍历两个数组的数， 每次先判断是否在字典里， 如果有， 则返回字典存储的下标值， 都没存就返回 -1 .

每次遍历看其返回值是否相同， 如果两个数组匹配， 即相同字符的下标都一样，则继续。 不同则退出。

`Python代码：`
```Python []
import sys
input = lambda:sys.stdin.readline().strip()
for _ in range(int(input())):
    def is_matching(t, s):
        if len(t) != len(s):
            return False
        num = {}
        char = {}
        for i in range(n):
            v1 = num.get(t[i], -1)
            v2 = char.get(s[i], -1)
            if v1 != v2:
                return False
            num[t[i]] = i
            char[s[i]] = i
        return True

    n = int(input())
    t = list(map(int, input().split()))
    m = int(input())

    for _ in range(m):
        s = input()
        if is_matching(t, s):
            print("YES")
        else:
            print("NO")
```
<br></br>

>  [D、Right Left Wrong](https://codeforces.com/contest/2000/problem/D)

**思路:** 最优情况是第一次选中间的 LR， 之后依次向外找匹配的 LR。 

可以反过来， 找最外边的 LR， 再依次向内部找。 这就可以用双指针来解决。

对于区间值的处理， 明显的前缀和数组， 方便在短时间内查询。

`Python代码：`
```Python []
import sys
input = lambda:sys.stdin.readline().strip()
for _ in range(int(input())):

    n = int(input())
    a = [0] + list(map(int, input().split()))
    s = list(input())
    
    # 处理前缀和，方便直接算答案
    for i in range(1, n + 1):
        a[i] += a[i - 1]

    l, r = 0, n - 1
    res = 0
    while l < r:
        while l < n and s[l] != 'L':
            l += 1
        while r >= 0 and s[r] != 'R':
            r -= 1
        if l < r:
            res += a[r + 1] - a[l]
            l += 1
            r -= 1
       
    print(res)
```
<br></br>

>  [E、Photoshoot for Gorillas](https://codeforces.com/contest/2000/problem/E)

**思路:** 啊， 猴子， 最崩的一集。 脑子里想的是深度学习的卷积运算。

统计每个格子被遍历的次数， 存于一个一维数组中， 对其进行排序。

再对猴子的 val 值排序， 将高个放在遍历次数多的格子里， 依次累加值。

`Python代码：`
```Python []
t = int(input())  
for _ in range(t):
    n, m, k = map(int, input().split())  
    w = int(input())  
    a = list(map(int, input().split()))  

    counts = []
    for i in range(n):
        for j in range(m):
            counts.append((min(n - k, i) - max(0, i - k + 1) + 1) * (min(m - k, j) - max(0, j - k + 1) + 1)) 
            
    a.sort(reverse=True)
    counts.sort(reverse=True)
    
    total = 0
    for i in range(w):
        total += counts[i] * a[i]

    print(total)
```
<br></br>

>  [F、Color Rows and Columns](https://codeforces.com/contest/2000/problem/F)

**思路:** 对每个矩形依次计算染色得到 1 ~ k 分的 cost。

用两个数组，分别记录读取每个矩形时， 每次的情况。 

来计算已经得到的分数和还需要得到的分数， 所需要的最小开销。

`Python代码：`
```Python []
import sys
input = lambda:sys.stdin.readline().strip()
inf = 10 ** 7
for _ in range(int(input())):
    n, k = map(int, input().split())
    dp = [inf] * (k + 1)
    dp[0] = 0
    for _ in range(n):
        ndp = dp[:]
        x, y = map(int, input().split())
        cost = [inf] * (x + y + 1)
        for i in range(x + 1):  # 计算获得 i + j 分的开销
            for j in range(y + 1):
                cost[i + j] = min(cost[i + j], i * y + j * x - i * j)

        for i in range(k + 1):# 已有分数
            for j in range(x + y + 1):# 还需要获得几分
                if i + j > k: break
                ndp[i + j] = min(ndp[i + j], dp[i] + cost[j])
        
        dp = ndp
    print(dp[k] if dp[k] < inf else '-1')
```
<br></br>

>  [G、Call During the Journey](https://codeforces.com/contest/2000/problem/G)

**思路:** 用两次 dij 的堆优化来做。

找出每个顶点的最大时间 𝑎𝑛𝑠𝑖 ，在这个时间点上可以离开顶点并在时间 𝑡0 到达顶点 𝑛。

找到这个值，从最后一个顶点运行Dijkstra算法。

在处理下一个边缘时，检查在 𝑎𝑛𝑠𝑣−𝑙𝑖1到 𝑎𝑛𝑠𝑣 的时间间隔内是否可以乘公交车出行。

如果可能的话，我们将乘公共汽车旅行;否则，我们要么步行，要么在这个点等待，然后乘公共汽车去。

`Python代码：`
```Python []
import sys
input = lambda:sys.stdin.readline().strip()
from heapq import heappop, heappush,heapify
inf = 10 ** 16
for _ in range(int(input())):
    n, m = map(int, input().split())
    t0, t1, t2 = map(int, input().split())
    path1 = [[] for _ in range(n)]
    path2 = [[] for _ in range(n)]
    
    for _ in range(m):
        u, v, l1, l2 = map(int, input().split())
        u -= 1
        v -= 1
        path1[u].append(l1 * n + v)
        path1[v].append(l1 * n + u)
        path2[u].append(l2 * n + v)
        path2[v].append(l2 * n + u)
    
    dis2 = [inf] * n
    dis2[n - 1] = 0
    
    hpq = [n - 1]
    while hpq:
        d, u = divmod(heappop(hpq), n)
        if dis2[u] == d:
            for msk in path1[u]:
                l, v = divmod(msk, n)
                if dis2[u] + l < dis2[v]:
                    dis2[v] = dis2[u] + l
                    heappush(hpq, dis2[v] * n + v)
    
    if dis2[0] <= t0 - t2:
        print(t0 - dis2[0])
    else:
        for i in range(n):
            if dis2[i] > t0 - t2:
                dis2[i] = inf
        hpq = [dis2[i] * n + i for i in range(n) if dis2[i] <= t0 - t2]
        heapify(hpq)
        while hpq:
            d, u = divmod(heappop(hpq), n)
            if dis2[u] == d:
                for msk in path2[u]:
                    l, v = divmod(msk, n)
                    if dis2[u] + l < dis2[v]:
                        dis2[v] = d + l
                        heappush(hpq, dis2[v] * n + v)
                d = max(d, t0 - t1)
                for msk in path1[u]:
                    l, v = divmod(msk, n)
                    if d + l < dis2[v]:
                        dis2[v] = d + l
                        heappush(hpq, dis2[v] * n + v)
        print(max(-1, t0 - dis2[0]))
```
<br></br>
## 题目

| 题号 | 题目 | 链接 |
|-|-|-|
| A | Primary Task | [A、Primary Task](https://codeforces.com/contest/2000/problem/A) |
| B | Seating in a Bus | [B、Seating in a Bus](https://codeforces.com/contest/2000/problem/B) |
| C | Numeric String Template | [C、Numeric String Template](https://codeforces.com/contest/2000/problem/C) |
| D | Right Left Wrong | [D、Right Left Wrong](https://codeforces.com/contest/2000/problem/D) |
| E | Photoshoot for Gorillas | [E、Photoshoot for Gorillas](https://codeforces.com/contest/2000/problem/E) |
| F | Color Rows and Columns | [F、Color Rows and Columns](https://codeforces.com/contest/2000/problem/F) |
| G | Call During the Journey | [G、Call During the Journey](https://codeforces.com/contest/2000/problem/G) |
