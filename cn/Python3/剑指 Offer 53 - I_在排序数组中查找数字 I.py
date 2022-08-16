# @algorithm @lc id=100329 lang=python3 
# @title zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof


import math
from cn.Python3.mod.preImport import *
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        二分查找
        '''

        i, j = 0, len(nums)-1

        # 第一轮二分查找，找到target上界
        while i<=j:
            middle = math.floor((i+j)/2)

            if nums[middle] > target:
                j = middle-1
            else:
                i = middle+1

        right = i

        if j>=0 and nums[j] != target:
            return 0

        i = 0
        while i<=j:
            middle = math.floor((i+j)/2)

            if nums[middle] >= target:
                j = middle-1
            else:
                i = middle+1

        left = j

        return right-left-1
