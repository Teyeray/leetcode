# @nc app=nowcoder id=d77d11405cc7470d82554cb392585106 topic=13 question=11174 lang=Python3
# 2025-08-26 03:10:05
# https://www.nowcoder.com/practice/d77d11405cc7470d82554cb392585106?tpId=13&tqId=11174
# [JZ31] 栈的压入、弹出序列

# @nc code=start

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param pushV int整型一维数组 
# @param popV int整型一维数组 
# @return bool布尔型
#
class Solution:
    def IsPopOrder(self , pushV: List[int], popV: List[int]) -> bool:
        # write code here
        res = []
        while pushV:
            res.append(pushV.pop(0))
            while res and res[-1] == popV[0]:
                res.pop()
                popV.pop(0)
        return not popV
            


            

# @nc code=end
