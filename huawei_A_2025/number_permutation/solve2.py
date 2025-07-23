import sys
def add_number(nums:list):
    laizi_pairs = {2: 5, 5: 2, 6: 9, 9: 6}
    if (2 in nums and 5 in nums) or (6 in nums and 9 in nums) or (0 in nums):
        print('-1')
        sys.exit()
    nums.sort()
    return nums, laizi_pairs

def dfs(nums:list, used:set, path:str, laizi_pairs:dict, res:list):
    if path:
        res.append(int(path))
    if len(path) == len(nums):
        return
    for num in nums:
        if num in used:
            continue
        used.add(num)
        dfs(nums, used, path + str(num), laizi_pairs, res)
        if num in laizi_pairs and laizi_pairs[num] not in used:
            dfs(nums, used, path + str(laizi_pairs[num]), laizi_pairs, res)
        used.remove(num)

def main():
    nums = list(map(int, input().strip().split(",")))
    nums, laizi_pairs = add_number(nums)
    max_num = nums[-1]
    result = []
    dfs(nums, set(), "", laizi_pairs, result)
    if not result:
        print(-1)
        return
    print(sorted(result)[max_num - 1])

if __name__ == "__main__":
    main()