# @nc app=nowcoder id=c6c7742f5ba7442aada113136ddea0c3 topic=13 question=11160 lang=Python3
# 2025-07-27 14:58:59
# https://www.nowcoder.com/practice/c6c7742f5ba7442aada113136ddea0c3?tpId=13&tqId=11160
# [JZ10] 斐波那契数列

# @nc code=start

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param n int整型 
# @return int整型
#
class Solution:
    def Fibonacci(self , n: int) -> int:
        # write code here
        if n == 1 or n == 2:
            return 1
        a, b = 1, 1
        for _ in range(3, n + 1):
            a, b = b, a+b
        return b
# @nc code=end