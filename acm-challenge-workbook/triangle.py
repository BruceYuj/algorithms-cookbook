"""
题目：三角形
题意：n个棍子，棍子i的长度为ai.选出3根组成长度最长的三角形。弱无法组成三角形则输出0.
限制条件： 3 <= n <= 100   1 <= ai <= 10**6
分析：3根棍子能组成三角形的充要条件是： 最长棍子长度 < 另外两根之和
      所以，我们可以先将棍子按照长度排序（O(nlogn)），然后处理。
      时间复杂度为: Cnlogn+C1,也就是 O(nlogn).
"""

def longest_triangle(n, a):
    a.sort(reverse=True)
    for i in range(n-2):
        if a[i] < (a[i+1]+a[i+2]):
            return a[i]+a[i+1]+a[i+2]
    return 0

#测试
print("test 1:")
n = 5
a = [2, 3, 4, 5, 10]
print(longest_triangle(n, a))

print("test 2:")
n = 4
a = [4, 5, 10, 20]
print(longest_triangle(n, a))