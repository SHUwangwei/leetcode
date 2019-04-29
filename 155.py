class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = float('inf')
        self.minlist = []
        self.stack = []
        self.length = 0

    def push(self, x):

        self.stack.append(x)
        self.length += 1
        if self.length == 1:
            self.min = x
            self.minlist.append(x)
        elif x <= self.min:
            self.min = x
            self.minlist.append(x)

    def pop(self):
        changeflag = False
        if self.length > 0:
            if self.stack[-1] == self.min:
                del self.minlist[-1]
                changeflag = True
            del self.stack[-1]
            self.length -= 1
            if changeflag:
                if self.length > 0:
                    self.min = self.minlist[-1]
                else:
                    self.min = float('inf')

    def top(self):
        if self.length > 0:
            return self.stack[-1]

    def getMin(self):
        if self.length > 0:
            return self.min
