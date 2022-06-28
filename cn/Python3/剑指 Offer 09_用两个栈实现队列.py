# @algorithm @lc id=100273 lang=python3 
# @title yong-liang-ge-zhan-shi-xian-dui-lie-lcof

class CQueue:

    def __init__(self):
        # A栈作为主队列的实现，B栈作为过渡栈实现队列的头尾功能
        self.A, self.B = [], []


    def appendTail(self, value: int) -> None:
        # 本质上是列表，直接append队尾即可
        self.A.append(value)


    def deleteHead(self) -> int:
        # 将B栈作为过渡栈，B中的头元素一定是A栈中的头部元素
        # if self.B != []:
        #     return self.B.pop()
        # elif self.A == []:
        #     return -1
        # else:
        #     for _ in range(len(self.A)):
        #         self.B.append(self.A.pop())
        #     return self.B.pop()
        if self.A == []:
            return -1
        else:
            return self.A.pop(0)

        
    '''
    思路整理：
        1. 双栈实现一个队列
        2. 队尾添加的功能由于底层是list实现，则直接在队尾append即可
        3. list.pop()默认删除最后一个元素，可以利用B栈实现A栈的倒序，即B栈头=A栈底=队列头
        4. 队头删除存在三种情况：
            1) B栈不空，则存在之前已经倒序的队，直接弹出B栈底元素
            2) A栈空，直接返回-1
            3) 倒序现有栈，弹出队尾元素
    '''



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()