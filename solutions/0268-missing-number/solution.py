class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        self.nums=nums
        self.nums.sort()
        b=int
        for x in range(len(self.nums)-1):
            if self.nums[x+1] - self.nums[x] != 1:
                b=self.nums[x]+1
        if len(self.nums)!=self.nums[-1]:
            b=self.nums[-1]+1
        if self.nums[0]!=0:
            b=0

        return b
