nums = input().strip().split()
nums = [int(x) for x in nums]
print(f'nums:{nums}')
def largestNumber(nums):
    dp = [num for num in nums]
    for i in range(1,len(nums)):
        for j in range(len(nums)-1,_ ,-1):
            a = int(str(dp[j-1])+str(nums[j]))
            b = int(str(nums[j])+str(dp[j-1]))
            print(f'\nin i:{i}, j:{j}, dp: {dp}, a: {a}, b: {b}')
            dp[j] = max(int(dp[j]), max(a,b))
            print(f'dp_calculated: {dp}\n')
    return str(max(dp))
    
print(largestNumber(nums))
