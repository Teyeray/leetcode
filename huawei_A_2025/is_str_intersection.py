from typing import Dict, Tuple
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"  # 预期返回 True，因为 s3 可以由 s1 和 s2 交错组成

def is_interleave(s1:str , s2:str , s3:str) -> bool:
    ls1, ls2 = len(s1), len(s2)
    if len(s1) + len(s2) != len(s3):
        return False
    memo: Dict[Tuple[int, int], bool] = {}  

    def dfs(i:int , j:int) -> bool:
        if i == len(s1) and j == len(s2):
            return True
        if (i,j) in memo:
            return memo[(i,j)]
        k = i + j
        if i < ls1 and s1[i] == s3[k]:
            if dfs(i+1, j):
                memo[(i,j)] = True
                return True
        if j < ls2 and s2[j] == s3[k]:
            if dfs(i, j+1):
                memo[(i,j)] = True
                return True
        memo[(i,j)] = False
        return False
    
    result = dfs(0, 0)
    print(f'memo:{memo}')
    return result

if is_interleave(s1, s2, s3):
    print("yes")
else:
    print("no")
        