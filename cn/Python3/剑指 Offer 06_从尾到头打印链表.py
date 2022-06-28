# @algorithm @lc id=100282 lang=python3 
# @title cong-wei-dao-tou-da-yin-lian-biao-lcof


from cn.Python3.mod.preImport import *
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
# @test([1,3,2])=[2,3,1]
# @test([1,3,2])=[2,3,1]
    def reversePrint(self, head: ListNode) -> List[int]:
        stack = []
        # walk through all the link-list
        n = head
        while n is not None:
            stack.append(n.val)
            n = n.next
        
        # reverse the stack
        stack.reverse()

        return stack