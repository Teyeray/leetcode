# @nc app=nowcoder id=ef1f53ef31ca408cada5093c8780f44b topic=13 question=11166 lang=Python3
# 2025-08-15 23:14:38
# https://www.nowcoder.com/practice/ef1f53ef31ca408cada5093c8780f44b?tpId=13&tqId=11166
# [JZ21] 调整数组顺序使奇数位于偶数前面(一)

# @nc code=start

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param array int整型一维数组 
# @return int整型一维数组
#
class Solution:
    def reOrderArray(self , array: List[int]) -> List[int]:
        # write code here
        odd = [x for x in array if x % 2 == 1]
        even = [x for x in array if x % 2 == 0]
        return odd + even

# @nc code=end
