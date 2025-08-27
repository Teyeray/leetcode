# @nc app=nowcoder id=a861533d45854474ac791d90e447bafd topic=13 question=11176 lang=Python3
# 2025-08-27 21:14:08
# https://www.nowcoder.com/practice/a861533d45854474ac791d90e447bafd?tpId=13&tqId=11176
# [JZ33] 二叉搜索树的后序遍历序列

# @nc code=start

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param sequence int整型一维数组 
# @return bool布尔型
#
class Solution:
    def VerifySquenceOfBST(self , sequence: List[int]) -> bool:
        # write code here
        if not sequence:
            return False


        def helper(seq):
            if len(seq) <= 1:
                return True
            root = seq[-1]

            for idx, num in enumerate(seq[:-1]):
                if num >= root:
                    break
            else:
                idx = len(seq) - 1
                
            left = seq[:idx]
            right = seq[idx:-1]
            for num in right:
                if num <= root:
                    return False
            return helper(left) and helper(right)
        return helper(sequence)
                

# @nc code=end
