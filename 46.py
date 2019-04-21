class Solution:
    def permute(self, nums):

        self.res = []
        length = len(nums)
        temp = []
        self.getresult(temp, nums, length)
        return self.res



    def getresult(self, temp, numsleft, length):
        if len(temp) == length:
            self.res.append(temp[:])
            return
        for num in numsleft:

            reslist = numsleft[:]
            temp.append(num)
            reslist.remove(num)
            self.getresult(temp, reslist, length)
            temp.pop()



s = Solution()

print(s.permute([1, 2, 3]))
        
         var  num_s = Number("1232134456.546 ");
         num_s = parseFloat(num_s.toFixed(2));
         console.log(num_s.toLocaleString());