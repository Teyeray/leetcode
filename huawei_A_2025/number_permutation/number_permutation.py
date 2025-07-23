import sys

def add_number(nums:list) -> list:
    laizi_pairs = {2: 5, 5: 2, 6: 9, 9: 6}
    if (2 in nums and 5 in nums) or (6 in nums and 9 in nums) or (0 in nums):
        print('-1')
        sys.exit()
    for i in range(len(nums)):
        if nums[i] in laizi_pairs:
            nums.append(laizi_pairs[nums[i]])
    return nums

def arrange_nums(nums):
    nums.sort()
    m = nums[-1]
    n = int(len(nums))
    memo = [False for _ in range(n)]
    result = []
    curr = []
    def backtrack(curr):
        if len(result) == m:
            return
        if len(curr) == j:
            result.append("".join(str(x) for x in curr))
            return
        for i in range(n):
            if not memo[i]:
                curr.append(nums[i])
                memo[i] = True
                backtrack(curr)
                curr.pop()
                memo[i] = False  
    for j in range(1,n):
        backtrack(curr)
    return result



nums = list(map(int, input().strip().split(",")))
#nums = [1,4,8,7]
nums = add_number(nums)
#print(f'nums:{nums}')
result = arrange_nums(nums)
#print(f'arrange_nums:{result}')

#ans
print(result[-1])
