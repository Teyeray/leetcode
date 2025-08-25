# @nc app=nowcoder id=d8b6b4358f774294a89de2a6ac4d9337 topic=13 question=11169 lang=Python3
# 2025-08-16 18:39:24
# https://www.nowcoder.com/practice/d8b6b4358f774294a89de2a6ac4d9337?tpId=13&tqId=11169
# [JZ25] 合并两个排序的链表

# @nc code=start

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param pHead1 ListNode类 
# @param pHead2 ListNode类 
# @return ListNode类
#
class Solution:
    def Merge(self , pHead1: ListNode, pHead2: ListNode) -> ListNode:
        # write code here
        dummy = ListNode(0)
        current = dummy
        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                current.next = pHead1
                pHead1 = pHead1.next
            else:
                current.next = pHead2
                pHead2 = pHead2.next
            current = current.next
        current.next = pHead1 or pHead2
        return dummy.next
# @nc code=end
