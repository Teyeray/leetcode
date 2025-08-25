# @nc app=nowcoder id=a9d0ecbacef9410ca97463e4a5c83be7 topic=13 question=11171 lang=Python3
# 2025-08-16 22:11:40
# https://www.nowcoder.com/practice/a9d0ecbacef9410ca97463e4a5c83be7?tpId=13&tqId=11171
# [JZ27] 二叉树的镜像

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
# @return TreeNode类
#
class Solution:
    def Mirror(self , pRoot: TreeNode) -> TreeNode:
        # write code here
        def exchange(Node: TreeNode):
            if Node == None:
                return
            Node.left, Node.right = Node.right, Node.left
            exchange(Node.left)
            exchange(Node.right)
            return
        exchange(pRoot)
        return pRoot
# @nc code=end
