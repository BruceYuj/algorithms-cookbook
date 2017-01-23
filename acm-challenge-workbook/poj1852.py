"""
题目：Ants
题意：n个蚂蚁以1cm/s在长为Lcm的杆上爬，蚂蚁爬到杆子断点端点就会掉下来。
      每个蚂蚁朝向不定，如果两只蚂蚁相遇，他们会各自反向爬回去。我们已知
      每只蚂蚁距离杆子左端xi。计算所有蚂蚁落下杆子所需的最短时间和最长时间。
限制条件：1 <= L <= 10**6  1 <= n <= 10**6  1 <= xi <= L
解题思路：就是蚂蚁的各个朝向组合最好情况和最差情况。
        最好情况：就是蚂蚁没有相遇，各自爬到终点。也就是1/2点的两边蚂蚁各自朝向相同
        最坏情况：就算蚂蚁相遇，我们假设他们没有返回，而是继续往前爬，各个蚂蚁距离两边终点
                  最大值的最大值。
        时间复杂度：O(n)
"""

def ants_walk_time(L, n, x):
    min_time = 0
    max_time = 0
    for i in x:
        if min_time < min(i, L-i):
            min_time = min(i, L-i)
        if max_time < max(i, L-i):
            max_time = max(i, L-i)
    return min_time, max_time

#test
L = 10
n = 3
x = [2, 6, 7]
print(ants_walk_time(L, n, x))


