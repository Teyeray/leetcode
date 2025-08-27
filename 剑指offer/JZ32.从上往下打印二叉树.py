# @nc app=nowcoder id=7fe2212963db4790b57431d9ed259701 topic=13 question=11175 lang=Python3
# 2025-08-27 19:31:12
# https://www.nowcoder.com/practice/7fe2212963db4790b57431d9ed259701?tpId=13&tqId=11175
# [JZ32] 从上往下打印二叉树

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
# @param root TreeNode类 
# @return int整型一维数组
#
class Solution:
    def PrintFromTopToBottom(self , root: TreeNode) -> List[int]:
        # write code here
        res = []
        curr = []
        if not root:
            return []
        curr.append(root)
        def Add_Node():
            while curr:
                node = curr.pop(0)
                res.append(node.val)
                if node.left:
                    curr.append(node.left)
                if node.right:
                    curr.append(node.right)
        Add_Node()
        return res
# @nc code=end
