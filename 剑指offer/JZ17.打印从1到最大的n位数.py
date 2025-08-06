# @nc app=nowcoder id=4436c93e568c48f6b28ff436173b997f topic=13 question=39281 lang=Python3
# 2025-08-06 17:03:54
# https://www.nowcoder.com/practice/4436c93e568c48f6b28ff436173b997f?tpId=13&tqId=39281
# [JZ17] 打印从1到最大的n位数

# @nc code=start

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param n int整型 最大位数
# @return int整型一维数组
#
class Solution:
    def printNumbers(self , n: int) -> List[int]:
        # write code here
        max_num = 10 ** n
        print(max_num)
        return range(1, max_num)

# @nc code=end
