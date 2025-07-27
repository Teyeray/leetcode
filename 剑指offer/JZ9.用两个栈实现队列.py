# @nc app=nowcoder id=54275ddae22f475981afa2244dd448c6 topic=13 question=11158 lang=Python3
# 2025-07-27 14:10:36
# https://www.nowcoder.com/practice/54275ddae22f475981afa2244dd448c6?tpId=13&tqId=11158
# [JZ9] 用两个栈实现队列

# @nc code=start

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        # write code here
        self.stack1.append(node)
    def pop(self):
        # return xx
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            return None
        return self.stack2.pop()
# @nc code=end
