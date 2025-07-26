# @nc app=nowcoder id=9023a0c988684a53960365b889ceaf5e topic=13 question=11210 lang=Python3
# 2025-07-26 23:33:25
# https://www.nowcoder.com/practice/9023a0c988684a53960365b889ceaf5e?tpId=13&tqId=11210
# [JZ8] 二叉树的下一个结点

# @nc code=start

# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    nodes = []
    def GetNext(self, pNode):
        # write code here
        root = pNode
        while root.next:
            root = root.next
        
        self.InOrder(root)
        for i in range(len(self.nodes) - 1):
            curr = self.nodes[i]
            if curr == pNode:
                return self.nodes[i + 1]
        return None
    
    def InOrder(self, root):
        if not root:
            return
        self.InOrder(root.left)
        self.nodes.append(root)
        self.InOrder(root.right)


# @nc code=end
