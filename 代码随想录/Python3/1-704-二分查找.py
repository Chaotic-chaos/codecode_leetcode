# -*- coding: utf-8 -*-
'''
Project:       ~/projects/leetcode/代码随想录/Python3
File Name:     1-704-二分查找.py
Author:        Chaos
Email:         life0531@foxmail.com
Date:          2023/04/08
Software:      Vscode
'''

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        res = -1
        while left <= right:
            mid = (right+left)//2
            if nums[mid] == target:
                res = mid
                break

            if nums[mid] > target:
                right = mid-1

            if nums[mid] < target:
                left = mid+1

        return res


if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    
    solution = Solution()

    print(solution.search(nums, target=2))
