# [AtCoder Beginner Contest 365](https://atcoder.jp/contests/abc365)
- 每道题目的链接在文末

- Date：2024.08.07

- 赛后模拟没有排名
  
       
---
> [A、Leap Year](https://atcoder.jp/contests/abc365/tasks/abc365_a)

**思路:** 判断满足`366`天的条件， 输出366。   

剩余情况统一输出 `365`。

`Python代码：`
```Python []
import sys
input = lambda:sys.stdin.readline().strip()

n = int(input())
if (n % 4 == 0 and n % 100) or n % 400 == 0:
    print('366')
else:
    print('365')
```
<br></br>

> [B、Second Best](https://atcoder.jp/contests/abc365/tasks/abc365_b)

**思路:** 将数组`元素值`和其`下标`存储到新数组`B`中， 对新数组按照从小到大，值为第一优先，下标为第二优先的规则排序。    

只需找出倒数第二个值的下标即可。   

这里用到python的特性，负下标访问

`Python代码：`
```Python []
import sys
input = lambda:sys.stdin.readline().strip()

n = int(input())
a = list(map(int, input().split()))
b = []
for i,x in enumerate(a):
    b.append([x,i + 1])
b.sort()
print(b[-2][1])
```
<br></br>

> [C、Transportation Expenses](https://atcoder.jp/contests/abc365/tasks/abc365_c)

**思路:** 考虑`infinite`的情况，只有所有人的交通费用和都小于等于补贴总额`m`时，补贴可以无限大。   

当不满足上述情况时，补贴限额将小于最大交通费用

用二分找出位于`1`和`max(a)`之间的交通补贴`x`，看是否满足情况。

输出满足情况的最大值

`Python代码：`
```Python []
import sys
input = lambda:sys.stdin.readline().strip()

n, m = map(int, input().split())
c = list(map(int, input().split()))

def check(x):
    s = 0
    for i in range(n):
        s += min(c[i], x)
    if s <= m:
        return True
    return False 

if m >= sum(c):
    print('infinite')
else:
    l, r = 0, max(c)
    while l < r:
        mid = (l + r + 1) >> 1
        if check(mid):
            l = mid
        else:
            r = mid - 1
    print(l)
```
<br></br>

>  [D、AtCoder Janken 3](https://atcoder.jp/contests/abc365/tasks/abc365_d)

**思路:** 将石头剪刀纸分别抽象成数字

石头 `R`抽象成`0`, 纸`P`抽象成`1`，剪刀`S`抽象成`2`。

这样可以通过 `(k + 1) % 3` 来判断是不是能赢或者不能赢

遍历数组`s`，找到对手目前的情况，再分别遍历上一次我方的情况，和这一次我方的情况。

如果上一次和这一次的情况不一样，当对手不能赢我方时，我方可以通过判断`k`能否赢得对手来决定是否 `+ 1`。

最后dfs第一局出剪刀，石头，纸这三种情况，并打印三种情况的最大值。

`Python代码：`
```Python []
import sys
input = lambda:sys.stdin.readline().strip()

n, m = map(int, input().split())
c = list(map(int, input().split()))

def check(x):
    s = 0
    for i in range(n):
        s += min(c[i], x)
    if s <= m:
        return True
    return False 

if m >= sum(c):
    print('infinite')
else:
    l, r = 0, max(c)
    while l < r:
        mid = (l + r + 1) >> 1
        if check(mid):
            l = mid
        else:
            r = mid - 1
    print(l)
```
<br></br>


>   [E、Xor Sigma Problem](https://atcoder.jp/contests/abc365/tasks/abc365_e)

**思路:** 通过每一位的二进制表示，来分别计算每一个位次的情况。

先遍历每个位次的可能情况。

再遍历数组，如果当前位为1， 那么以1结尾的子序列数量为`(j - 1 - f[j - 1])`, 如果为0. 以0结尾的子序列数量为`f[j - 1]`

判断结束之后，答案加上`当前位次的值 * 子序列数量`， 再将当前值为1的子序列的数量 `+1` 。

输入答案即可。

`Python代码：`
```Python []
import sys
input = lambda:sys.stdin.readline().strip()

n = int(input())
a = [0] + list(map(int, input().split()))

f = [0] * (n + 1)
ans = 0
for i in range(30):
    for j in range(1, n + 1):
        b = (a[j] >> i)&1 #当前位是1
        f[j] = (j - 1 - f[j - 1]) if b else f[j - 1]
        ans += (1 << i) * f[j]
        f[j] += b
print(ans)

```
<br></br>
## 题目

| 题号 | 问题 | 链接 |
|-|-|-|
| A | Leap Year | [A、Leap Year](https://atcoder.jp/contests/abc365/tasks/abc365_a) |
| B | Second Best | [B、Second Best](https://atcoder.jp/contests/abc365/tasks/abc365_b) |
| C | Transportation Expenses | [C、Transportation Expenses](https://atcoder.jp/contests/abc365/tasks/abc365_c) |
| D | AtCoder Janken 3 | [D、AtCoder Janken 3](https://atcoder.jp/contests/abc365/tasks/abc365_d) |
| E | Xor Sigma Problem | [E、Xor Sigma Problem](https://atcoder.jp/contests/abc365/tasks/abc365_e) |
| F | Takahashi on Grid | [F、Takahashi on Grid](https://atcoder.jp/contests/abc365/tasks/abc365_f) |
| G | AtCoder Office | [G、AtCoder Office](https://atcoder.jp/contests/abc365/tasks/abc365_g) |

