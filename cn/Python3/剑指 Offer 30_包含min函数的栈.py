# @algorithm @lc id=100302 lang=python3 
# @title bao-han-minhan-shu-de-zhan-lcof

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.help = []


    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.help == [] or x < self.help[-1]:
            self.help.append(x)


    def pop(self) -> None:
        res = self.stack.pop()
        if self.help[-1] == res:
            self.help.pop()


    def top(self) -> int:
        return self.stack[-1]


    def min(self) -> int:
        return self.help[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
