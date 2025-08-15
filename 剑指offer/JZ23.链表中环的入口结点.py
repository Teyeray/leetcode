# @nc app=nowcoder id=253d2c59ec3e4bc68da16833f79a38e4 topic=13 question=11208 lang=Python3
# 2025-08-16 02:00:04
# https://www.nowcoder.com/practice/253d2c59ec3e4bc68da16833f79a38e4?tpId=13&tqId=11208
# [JZ23] 链表中环的入口结点

# @nc code=start

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        p, q = pHead, pHead
        while p and q and p.next:
            p = p.next.next
            q = q.next
            if q == p:
                p = pHead
                while p != q:
                    p = p.next
                    q = q.next
                return p
        return None
# @nc code=end
