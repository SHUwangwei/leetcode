class RLEIterator:

    def __init__(self, A):
        self.input = A
        self.length = len(A)

    def next(self, n):
        last = -1
        while n > 0 and self.length > 1:
            if self.input[0] > n:
                last = self.input[1]
                self.input[0] -= n
                break
            elif self.input[0]  == n:
                last = self.input[1]
                del self.input[0]
                del self.input[0]
                self.length -= 2
                break
            else:
                self.


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)