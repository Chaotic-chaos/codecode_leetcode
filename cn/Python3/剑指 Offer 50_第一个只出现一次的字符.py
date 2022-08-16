# @algorithm @lc id=100316 lang=python3 
# @title di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof


import re
from cn.Python3.mod.preImport import *
class Solution:
    def firstUniqChar(self, s: str) -> str:
        if s == "":
            return " "
        
        res_dict = {}
        for c in s:
            res_dict[c] = res_dict.get(c, 0) + 1

        for k, v in res_dict.items():
            if v == 1:
                return k

        return " "
