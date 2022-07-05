# @algorithm @lc id=100280 lang=python3 
# @title ti-huan-kong-ge-lcof


import re
from cn.Python3.mod.preImport import *
class Solution:
    def replaceSpace(self, s: str) -> str:
        return re.sub("[ ]", "%20", s)