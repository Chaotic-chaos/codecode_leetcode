# @algorithm @lc id=100300 lang=python3 
# @title fu-za-lian-biao-de-fu-zhi-lcof


from cn.Python3.mod.preImport import *
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        '''
        个人尝试思路：
            1. 使用辅助栈存储所有已复制节点
            2. 遍历旧链表，根据random指针重建新链表的random指针
            🚨完全无法获取到同val节点的先后关系，无法有效重建random指针
        '''

        '''
        官解思路：
            1. 使用字典建立{旧节点：新节点}映射关系
            2. 遍历字典，根据旧的节点指针关系重建新的节点指针关系
        '''
        current = head
        dict_map = {}
        while current:
            dict_map[current] = Node(current.val, None, None)
            current = current.next

        for old, new in dict_map.items():
            new.next = dict_map.get(old.next)
            new.random = dict_map.get(old.random)

        return list(dict_map.values())[0]
