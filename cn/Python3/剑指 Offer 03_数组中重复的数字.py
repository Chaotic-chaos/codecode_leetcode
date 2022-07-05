# @algorithm @lc id=100275 lang=python3 
# @title shu-zu-zhong-zhong-fu-de-shu-zi-lcof


from cn.Python3.mod.preImport import *
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        # 自己的题解，超时
        # for i in range(len(nums)):
        #     char = nums.pop(0)
        #     if char in nums:
        #         return char
            
        # return None


        no_repeat = set()
        for i in nums:
            if i not in no_repeat:
                no_repeat.add(i)
            else:
                return i

        return None