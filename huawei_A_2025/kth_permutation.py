def backtracking(path, used, result, n, nums):
    if len(path) == n:
        result.append(path[:])
        #print(f'\n add result:{result}')
        return
    for i in range(len(used)):
        if used[i]:
            continue
        used[i] = True
        path.append(nums[i])
        #print(f'path:{path}, used:{used}')
        backtracking(path, used, result, n, nums)
        path.pop()
        used[i] = False

def permute(n) -> list:
    nums = list(range(n, 0, -1))
    result = []
    used = [False for _ in range(len(nums))]
    backtracking([], used, result, n, nums)
    return result

#input
n = int(input().strip())
k = int(input().strip())

#exp 0
# n = 4
# k = 3
result = permute(n)

#print(f'result:{result}')

print("".join(str(x) for x in result[-k]))
