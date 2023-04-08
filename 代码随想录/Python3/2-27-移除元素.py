# -*- coding: utf-8 -*-
'''
Project:       ~/projects/leetcode/代码随想录/Python3
File Name:     2-27-移除元素.py
Author:        Chaos
Email:         life0531@foxmail.com
Date:          2023/04/09
Software:      Vscode
'''

from cmath import inf
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Plan-1: O(n^2)
        # length_num = len(nums)
        # count = 0
        # for idx, n in enumerate(nums):
        #     if n == val:
        #         nums[idx] = +inf
        #         count += 1

        # nums.sort()

        # return length_num-count, nums

        # Plan-2: O(n)
        len_nums = len(nums)
        fast_p, slow_p = 0, 0

        while fast_p <= len_nums-1:
            if nums[fast_p] != val:
                nums[slow_p] = nums[fast_p]
                slow_p += 1
            fast_p += 1

        return slow_p


if __name__ == '__main__':
    nums = [0, 1, 2, 2, 3, 0, 4, 2]

    solution = Solution()

    print(solution.removeElement(nums=nums, val=2))
