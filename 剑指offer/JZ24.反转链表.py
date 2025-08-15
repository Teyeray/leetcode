# @nc app=nowcoder id=75e878df47f24fdc9dc3e400ec6058ca topic=13 question=11168 lang=Python3
# 2025-08-16 03:35:13
# https://www.nowcoder.com/practice/75e878df47f24fdc9dc3e400ec6058ca?tpId=13&tqId=11168
# [JZ24] 反转链表

# @nc code=start

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param head ListNode类 
# @return ListNode类
#
class Solution:
    def ReverseList(self , head: ListNode) -> ListNode:
        # write code here
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

# @nc code=end
