# @algorithm @lc id=100276 lang=python3 
# @title er-wei-shu-zu-zhong-de-cha-zhao-lcof


from cn.Python3.mod.preImport import *
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        '''
        个人思路：
            1. python内置关键字in
            2. 行遍历矩阵，使用关键字in判断整数是否存在
            3. O(n)
        '''

        for line in matrix:
            if target in line:
                return True

        return False