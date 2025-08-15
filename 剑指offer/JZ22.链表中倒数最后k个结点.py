# @nc app=nowcoder id=886370fe658f41b498d40fb34ae76ff9 topic=13 question=11167 lang=Python3
# 2025-08-16 00:21:02
# https://www.nowcoder.com/practice/886370fe658f41b498d40fb34ae76ff9?tpId=13&tqId=11167
# [JZ22] 链表中倒数最后k个结点

# @nc code=start

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param pHead ListNode类 
# @param k int整型 
# @return ListNode类
#
class Solution:
    def FindKthToTail(self , pHead: ListNode, k: int) -> ListNode:
        # write code here
        isend = True
        count = 0
        head = pHead
        if pHead is None:
            return None
        
        while isend:
            if pHead.next is None:
                isend = False
            else:
                pHead = pHead.next
            count += 1
        if k > count or k <= 0:
            return None
        if k == count:
            return head
        end = count - k
        print(f'count: {count}, k: {k}, end: {end}')
        count = 0
        curr = head
        while count < end:
            curr = curr.next
            print(f'curr: {curr.val if curr else None}, count: {count}')
            count += 1
        return curr
# @nc code=end
