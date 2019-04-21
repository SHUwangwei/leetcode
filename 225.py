class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stackdata = []

    def push(self, x):
        """
        Push element x onto stack.
        """
        self.stackdata.push(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        """
        top = self.stackdata.pop()
        return top

    def top(self):
        """
        Get the top element.
        """
        return self.stackdata[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        """
        self.stackdata.clear()
        return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()