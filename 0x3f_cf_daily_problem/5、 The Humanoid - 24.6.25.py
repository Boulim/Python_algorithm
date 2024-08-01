The Humanoid
"""
题目链接:
  Problem - 1759E - Codeforces
思路：（1500）
	对数组a先排序
	再对223，232，322这三种打针顺序取最大值
"""
Python代码:
import sys
input = lambda:sys.stdin.readline().strip()
for _ in range(int(input())):
    n,h = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    def killed(h,serum):
        cnt = 0
        i = 0
        for x in a:
            while x >= h:            
                if cnt < 3:
                    h *= serum[cnt]
                    cnt +=1
                else:
                    return i
            h += x // 2
            i += 1
        return i
    print(max(killed(h,[2,2,3]),killed(h,[2,3,2]),killed(h,[3,2,2])))

