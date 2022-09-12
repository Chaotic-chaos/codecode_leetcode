# @algorithm @lc id=100287 lang=python3 
# @title shu-de-zi-jie-gou-lcof


from asyncio import FastChildWatcher
from cn.Python3.mod.preImport import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        # if B is None:
        #     return False

        # # travel A-tree
        # a_tree = []
        # q = []
        # q.append(A)
        # while q != []:
        #     current_node = q.pop(0)
        #     a_tree.append(current_node.val)
        #     if current_node.left is not None:
        #         q.append(current_node.left)
        #     if current_node.right is not None:
        #         q.append(current_node.right)

        # # travel B-tree
        # b_tree = []
        # q = []
        # q.append(B)
        # while q != []:
        #     current_node = q.pop(0)
        #     b_tree.append(current_node.val)
        #     if current_node.left is not None:
        #         q.append(current_node.left)
        #     if current_node.right is not None:
        #         q.append(current_node.right)

        # def is_subtree(a, b):
        #     if len(a) != len(b):
        #         return False
        #     for elem_a, elem_b in zip(a, b):
        #         if elem_a != elem_b:
        #             return False
        #     return True

        # for index, elem in enumerate(a_tree):
        #     if elem == b_tree[0]:
        #         is_sub = is_subtree(a_tree[index:len(b_tree)], b_tree)

        #         if is_sub:
        #             return True
        #         else:
        #             continue

        # return False

        '''
        # 错误方案👆:
            1. 必须要边遍历，边判断
            2. 最优解是递归
            3. 遍历完成之后丢失了结构信息，无法完成题目给的示例
        '''

        '''
        官解👇:
        '''
        def check(self, s, t): # 这里 t 可能为空
            if not t:
                return True
            if not s:
                return False
            
            return s.val == t.val and self.check(s.left, t.left) and self.check(s.right, t.right)

        if not A or not B: return False
        return self.check(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

