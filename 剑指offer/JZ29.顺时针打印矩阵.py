# @nc app=nowcoder id=9b4c81a02cd34f76be2659fa0d54342a topic=13 question=11172 lang=Python3
# 2025-08-26 01:38:15
# https://www.nowcoder.com/practice/9b4c81a02cd34f76be2659fa0d54342a?tpId=13&tqId=11172
# [JZ29] 顺时针打印矩阵

# @nc code=start

# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        res = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        while top <= bottom and left <= right:
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1

            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1

            if top <= bottom:
                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1

            if left <= right:
                for row in range(bottom, top - 1, -1):
                    res.append(matrix[row][left])
                left += 1
        return res
# @nc code=end
