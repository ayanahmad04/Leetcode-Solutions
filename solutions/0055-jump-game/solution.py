class Solution:
    def canJump(self, nums: list[int]) -> bool:
        last_index = len(nums) - 1
        reachable = 0  # how far we can go so far
        
        for i in range(len(nums)):
            if i > reachable:
                return False
            reachable = max(reachable, i + nums[i])
            if reachable >= last_index:
                return True  
        
        return True

