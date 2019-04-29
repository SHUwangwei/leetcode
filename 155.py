class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = float('inf')
        self.second = float('inf')
        self.stack = []
        self.length = 0


    def push(self, x):
        self.stack.append(x)
        self.length += 1
        if x <= self.min:
            self.second = self.min
            self.min = x
        elif x < self.second:
            self.second = self.x


    def pop(self):
        if self.length > 0:
            if self.stack[-1] == self.min:
                self.min = self.second
            del self.stack[-1]
            self.length -= 1
        

    def top(self):
        if self.length > 0:
            return self.stack[-1]

    def getMin(self):
        if self.length > 0:
            return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()