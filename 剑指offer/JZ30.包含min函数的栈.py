# @nc app=nowcoder id=4c776177d2c04c2494f2555c9fcc1e49 topic=13 question=11173 lang=Python3
# 2025-08-26 02:45:23
# https://www.nowcoder.com/practice/4c776177d2c04c2494f2555c9fcc1e49?tpId=13&tqId=11173
# [JZ30] 包含min函数的栈

# @nc code=start

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.res = []
        self.min_val = []
    def push(self, node):
        # write code here
        if not self.min_val or self.min_val[-1] > node:
            self.min_val.append(node)
        else:
            self.min_val.append(self.min_val[-1])
        self.res.append(node)
    def pop(self):
        # write code here
        self.res.pop()
        self.min_val.pop()
    def top(self):
        # write code here
        if self.res:
            return self.res[-1]
    def min(self):
        # write code here
        if self.min_val:
            return self.min_val[-1]


# @nc code=end
