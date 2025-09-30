class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        self.re=0
        self.nums=nums
        for i in self.nums:
            self.re=self.re^i
        return self.re
