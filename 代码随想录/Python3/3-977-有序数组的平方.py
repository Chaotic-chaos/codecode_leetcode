# -*- coding: utf-8 -*-
'''
Project:       ~/projects/leetcode/代码随想录/Python3
File Name:     3-977-有序数组的平方.py
Author:        Chaos
Email:         life0531@foxmail.com
Date:          2023/04/09
Software:      Vscode
'''

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Plan-1: O(nlogn)
        # res = []
        # for i in nums:
        #     res.append(i**2)

        # res.sort()

        # return res

        # Plan-2: O(n)
        res = [0]*len(nums)
        left = 0
        right = len(nums)-1
        res_p = len(res)-1

        while left <= right:
            if nums[left]**2 < nums[right]**2:
                res[res_p] = nums[right]**2
                right -= 1
            elif nums[left]**2 >= nums[right]**2:
                res[res_p] = nums[left]**2
                left += 1

            res_p -= 1

        return res


if __name__ == '__main__':
    nums = [-7, -3, 2, 3, 11]
    solution = Solution()

    print(solution.sortedSquares(nums))
