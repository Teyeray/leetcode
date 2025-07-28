# @nc app=nowcoder id=57d85990ba5b440ab888fc72b0751bf8 topic=13 question=33257 lang=Python3
# 2025-07-28 10:29:30
# https://www.nowcoder.com/practice/57d85990ba5b440ab888fc72b0751bf8?tpId=13&tqId=33257
# [JZ14] 剪绳子

# @nc code=start

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param n int整型 
# @return int整型
#
class Solution:
    def cutRope(self , n: int) -> int:
        # write code here
        num3 = n // 3
        if n % 3 == 1:
            num3 -= 1
        n -= num3 * 3
        print(f'3:{num3}, n:{n}')
        num2 = n // 2 
        print(f'2:{num2}, n:{n}')
        return 3**num3 * 2**num2

# @nc code=end
