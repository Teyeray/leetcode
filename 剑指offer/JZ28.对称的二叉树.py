# @nc app=nowcoder id=ff05d44dfdb04e1d83bdbdab320efbcb topic=13 question=11211 lang=Python3
# 2025-08-25 22:46:53
# https://www.nowcoder.com/practice/ff05d44dfdb04e1d83bdbdab320efbcb?tpId=13&tqId=11211
# [JZ28] 对称的二叉树

# @nc code=start

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param pRoot TreeNode类 
# @return bool布尔型
#
class Solution:
    def isSymmetrical(self , pRoot: TreeNode) -> bool:
        # write code here
        is_legal = True
        def is_mirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)
        if not pRoot:
            return True
        return is_mirror(pRoot.left, pRoot.right)
# @nc code=end
