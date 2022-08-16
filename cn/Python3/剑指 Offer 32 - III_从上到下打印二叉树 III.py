# @algorithm @lc id=100314 lang=python3 
# @title cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof


from cn.Python3.mod.preImport import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        '''
        1. 正常的层序遍历
        2. 偶数层正常加入，奇数层反转列表
        '''
        if not root:
            return []

        queue = []
        queue.append(root)
        res = []
        epoch = 0

        while queue != []:
            tmp_r = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                tmp_r.append(node.val)

                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

            if epoch%2 == 1:
                tmp_r.reverse()

            res.append(tmp_r)
            epoch = epoch+1

        return res
