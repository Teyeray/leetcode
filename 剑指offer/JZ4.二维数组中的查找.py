# @nc app=nowcoder id=abc3fe2ce8e146608e868a70efebf62e topic=13 question=11154 lang=Python3
# 2025-07-25 14:05:57
# https://www.nowcoder.com/practice/abc3fe2ce8e146608e868a70efebf62e?tpId=13&tqId=11154
# [JZ4] 二维数组中的查找

# @nc code=start

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param target int整型 
# @param array int整型二维数组 
# @return bool布尔型
#
'''
[
[1,2,8,9],
[2,4,9,12],
[4,7,10,13],
[6,8,11,15]
]
'''
class Solution:
    def Find(self , target: int, array: List[List[int]]) -> bool:
        # write code here
        m = len(array)
        n = len(array[0])
        j = 0
        i = n - 1
        while i >= 0 and j < m:
            num = array[j][i]
            if num == target:
                return True
            elif num > target:
                i -= 1
            else:
                j += 1
        return False
# @nc code=end
