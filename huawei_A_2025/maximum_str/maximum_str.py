nums = input().strip().split()
nums = [int(x) for x in nums]
print(f'nums:{nums}')

def compare(x,y):
    x = str(x)
    y = str(y)
    if x+y > y+x:
        return -1
    elif x+y < y+x:
        return 1
    else:
        return 0
def largestNumber(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            k = compare(nums[i],nums[j])
            print(f'k={k}')
            if k == 1:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
    return(nums)
print(largestNumber(nums))
