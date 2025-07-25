# @nc app=nowcoder id=6fe361ede7e54db1b84adc81d09d8524 topic=13 question=11203 lang=Python3
# 2025-07-25 12:00:54
# https://www.nowcoder.com/practice/6fe361ede7e54db1b84adc81d09d8524?tpId=13&tqId=11203
# [JZ3] 数组中重复的数字

# @nc code=start

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param numbers int整型一维数组 
# @return int整型
#
class Solution:
    def duplicate(self , numbers: List[int]) -> int:
        # write code here
        deduplicated = {}
        repeat = 0
        for num in numbers:
            if not str(num).isdigit():
                return -1
            if num not in deduplicated:
                deduplicated[num] = 1
            else:
                return num
        return -1
# @nc code=end
