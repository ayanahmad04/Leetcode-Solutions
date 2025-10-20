class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 0:
            return [[]]
        
        permutations = []
        for i in range(len(nums)):
            current = nums[i]
            remaining = nums[:i] + nums[i+1:]
            for p in self.permute(remaining):  
                permutations.append([current] + p)
        return permutations

