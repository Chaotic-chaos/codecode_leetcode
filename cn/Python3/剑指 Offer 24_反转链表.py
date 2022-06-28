# @algorithm @lc id=100298 lang=python3 
# @title fan-zhuan-lian-biao-lcof


from cn.Python3.mod.preImport import *
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
# @test([1,2,3,4,5])=[5,4,3,2,1]
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
            
        if head.next == None:
            return head
        
        pre, current = None, head
        while current:
            tmp_node = current.next
            current.next = pre
            
            pre = current
            current = tmp_node

        return pre
