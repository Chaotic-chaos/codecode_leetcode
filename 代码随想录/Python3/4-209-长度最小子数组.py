# -*- coding: utf-8 -*-
'''
Project:       ~/projects/leetcode/代码随想录/Python3
File Name:     4-209-长度最小子数组.py
Author:        Chaos
Email:         life0531@foxmail.com
Date:          2023/04/09
Software:      Vscode
'''

from cmath import inf
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Plan-1: O(n^2)
        # min_sub_length = +inf
        # for start in range(len(nums)):
        #     for end in range(start, len(nums)+1):
        #         tmp_res = sum(nums[start:end])
        #         if tmp_res >= target:
        #             min_sub_length = min(min_sub_length, len(nums[start:end]))
        #             break

        # return min_sub_length if min_sub_length != +inf else 0

        # Plan-2: O(n)
        min_sub_length = +inf
        left = 0
        window_sum = 0
        for right in range(len(nums)):
            window_sum += nums[right]
            while window_sum >= target:
                min_sub_length = min(min_sub_length, len(nums[left:right+1]))
                # 移动左指针后需要重新计算，否则死循环
                window_sum -= nums[left]
                left += 1

        return min_sub_length if min_sub_length != +inf else 0


if __name__ == '__main__':
    nums = [2, 3, 1, 2, 4, 3]
    target = 7

    solution = Solution()

    print(solution.minSubArrayLen(nums=nums, target=target))
