#处理输入
n = int(input().strip())
nums = list(map(int, input().strip().split()))

# #exp
# n = 6
# nums = [1, -2, 3, 4, -9, 7]
# #output = 10

# #exp 2
# n = 5
# nums = [-9, 8, -12, 99, 5]
# #output = 117

nums_r = []
i = 0
max_left = 0
max_right = 0
n = len(nums)

def find_max_split_difference(nums):
    n = len(nums)
    max_left = 0
    max_right = 0
    for i in range(n):
        left_sum = sum(nums[:i])
        right_sum = sum(nums[i:])
        if right_sum >= max_right and -left_sum >= max_left:
            max_right = right_sum
            max_left = -left_sum
    return max_left, max_right

max_left, max_right = find_max_split_difference(nums)
print(f'{max_right + max_left}')