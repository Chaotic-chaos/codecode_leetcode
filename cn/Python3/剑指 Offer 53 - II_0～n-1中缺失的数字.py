# @algorithm @lc id=100331 lang=python3 
# @title que-shi-de-shu-zi-lcof


import math
from cn.Python3.mod.preImport import *
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        个人思路：二分法
            与官方思路相同，但是存在bug
        Bug：
            决定上下界交换的条件应该是长度元素是否相等，而非小于等于
        '''

        # i, j = 0, len(nums)-1

        # while i<=j:
        #     middle = math.floor((i+j)/2)

        #     if len(nums[i:middle]) <= middle-1:
        #         j = middle-1
        #     else:
        #         i = middle+1

        # return nums[i]+1

        '''
        官解：由于是连续的数组，所以应直接使用元素与索引值比较
        '''
        i, j = 0, len(nums)-1

        while i<=j:
            middle = math.floor((i+j)/2)

            if nums[middle] == middle:
                i = middle+1
            else:
                j = middle-1

        return i