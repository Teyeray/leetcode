# @nc app=nowcoder id=2a49359695a544b8939c77358d29b7e6 topic=13 question=11218 lang=Python3
# 2025-07-27 22:57:10
# https://www.nowcoder.com/practice/2a49359695a544b8939c77358d29b7e6?tpId=13&tqId=11218
# [JZ12] 矩阵中的路径

# @nc code=start

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param matrix char字符型二维数组 
# @param word string字符串 
# @return bool布尔型
#
class Solution:
    def hasPath(self , matrix: List[List[str]], word: str) -> bool:
        # write code here
        rows, cols = len(matrix), len(matrix[0])
        def dfs(r, c, k):
            if r < 0 or r >= rows or c < 0 or c >= cols or matrix[r][c] != word[k]:
                return False
            if k == len(word) - 1:
                return True      
            tmp = matrix[r][c]
            matrix[r][c] = '#'
            res = (
                dfs(r + 1, c, k + 1) or
                dfs(r, c + 1, k + 1) or
                dfs(r - 1, c, k + 1) or
                dfs(r, c - 1, k + 1)
            )
            matrix[r][c] = tmp
            return res
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False
# @nc code=end
