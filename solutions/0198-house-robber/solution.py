class Solution:
    def rob(self, nums: list[int]) -> int:
        prev = curr = 0
        for amount in nums:
            prev, curr = curr, max(curr, prev + amount)
        return curr

