# @nc app=nowcoder id=6e196c44c7004d15b1610b9afca8bd88 topic=13 question=11170 lang=Python3
# 2025-08-16 18:56:46
# https://www.nowcoder.com/practice/6e196c44c7004d15b1610b9afca8bd88?tpId=13&tqId=11170
# [JZ26] 树的子结构

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
# @param pRoot1 TreeNode类 
# @param pRoot2 TreeNode类 
# @return bool布尔型
#
class Solution:
    def HasSubtree(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B:
            return False
        return self.compare(A, B) or self.HasSubtree(A.left, B) or self.HasSubtree(A.right, B)
    def compare(self, a: TreeNode, b: TreeNode):
        if not b:
            return True
        if not a or a.val != b.val:
            return False
        return self.compare(a.left, b.left) and self.compare(a.right, b.right)
        

                

# @nc code=end
