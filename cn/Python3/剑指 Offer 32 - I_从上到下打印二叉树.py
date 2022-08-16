# @algorithm @lc id=100311 lang=python3 
# @title cong-shang-dao-xia-da-yin-er-cha-shu-lcof


from cn.Python3.mod.preImport import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
            
        # 二叉树的层序遍历，借助队列实现
        temp_queue = []
        res = []

        temp_queue.append(root)
        while temp_queue != []:
            node = temp_queue.pop(0)

            res.append(node.val)

            if node.left is not None:
                temp_queue.append(node.left)
            if node.right is not None:
                temp_queue.append(node.right)

        return res