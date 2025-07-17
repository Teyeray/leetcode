'''
描述：
音乐课上，老师将 n 位同学排成一排。老师希望在不改变同学相对位置的前提下，
从队伍中选出最少数量的同学，使得剩下的同学排成合唱队形。

记合唱队形中一共有 k 位同学，记编号为 1,2,…,k，第 i 个人的身高为 h_i。要求：
  存在一位同学编号为 i（1 < i < k），使得
    h₁, h₂, …, h_{i-1}, h_i 严格递增；
    h_i, h_{i+1}, …, h_k 严格递减；
  即 h₁ < h₂ < … < h_{i-1} < h_i > h_{i+1} > … > h_k。

你能帮助老师计算，最少需要出列多少位同学，才能使得剩下的同学排成合唱队形？

输入描述：
  第一行输入一个整数 n（1 ≤ n ≤ 3000），代表同学数量。
  第二行输入 n 个整数 h₁, h₂, …, h_n（0 ≤ h_i ≤ 10⁵），代表每一位同学的身高。

输出描述：
  输出一个整数，代表最少需要出列的同学数量。
8
186 186 150 200 160 130 197 200
输出：
4

11
123 124 121 125 23 8 129 135 134 139 128
输出：
4
'''

#第一个解法（超时）
'''

import sys

lines = []
for line in sys.stdin:
    line = [int(x) for x in line.strip().split()]
    lines.extend(line)
tot_num = int(lines.pop(0))
line = lines
#print(f'line:{line}')
dp_left = [1] * tot_num
dp_right = [1] * tot_num
result = [0] * tot_num
for i in range(1, tot_num-1):
    for j in range(0, i):
        if line[i] > line[j]:
            dp_left[i] = max(dp_left[i], dp_left[j] + 1)
    for j in range(tot_num-1, tot_num-i-1, -1):
        if line[tot_num - i - 1] > line[j]:
            dp_right[tot_num-i-1] = max(dp_right[tot_num-i-1], dp_right[j] + 1)
for i in range(tot_num):
    result[i] = dp_left[i] + dp_right[i] - 1
print(f'{tot_num-max(result)}')

'''
#第二个解法
import sys

lines = []
dp_left = []
lis_left = []
dp_right = []
lis_right = []
result = []

for line in sys.stdin:
    line = [int(x) for x in line.strip().split()]
    lines.extend(line)
n = lines.pop(0)
print(f'n: {n},\nlines: {lines}')

def find_index(num, input_list):
    left, right = 0, len(input_list)
    while left < right:
        mid = (left + right) // 2
        if input_list[mid] < num:
            left = mid + 1
        else:
            right = mid
    return left

def get_sequence(input_list):
    dp = []
    lis1 = []
    lis = []
    parent = [-1] * len(input_list)
    real_dp = []
    for id, num in enumerate(input_list):
        left_index = find_index(num, dp)
        if left_index == len(dp):
            dp.append(num)
            lis1.append(id)
        else:
            dp[left_index] = num
            lis1[left_index] = id
        if left_index > 0:
            parent[id] = lis1[left_index - 1]
        lis.append(left_index + 1)
    curr = lis1[-1]
    while curr != -1:
        real_dp.append(input_list[curr])
        curr = parent[curr]
    return dp, lis, real_dp[::-1]


dp_left, lis_left, real_dp_left = get_sequence(lines[:n+1])
#flip the list for right sequence
lines_reversed = lines[::-1]
dp_right, lis_right, real_dp_right = get_sequence(lines_reversed)
real_dp_right = real_dp_right[::-1]
lis_right = lis_right[::-1]
max_keep = 0
for i in range(n):
    total = lis_left[i] + lis_right[i] - 1
    if total > max_keep:
        max_keep = total
print(f'{n-max_keep}')
print('-----------------------')
print(f'dp_left: {dp_left}, \nlis_left: {lis_left}, \n\nreal_dp_left: {real_dp_left}\n')
print(f'dp_right: {dp_right}, \nlis_right: {lis_right}, \n\nreal_dp_right: {real_dp_right}\n')
