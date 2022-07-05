# @algorithm @lc id=100330 lang=python3 
# @title zuo-xuan-zhuan-zi-fu-chuan-lcof


from cn.Python3.mod.preImport import *
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        if len(s) == 1:
            return s

        s = list(s)
        chars = s[:n]
        s = s[n:]
        s += chars
        
        return "".join(s)