class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums_dict=dict.fromkeys(nums,0)
        for i in nums:
            nums_dict[i]+=1
        maxi=max(nums_dict.values())
        for key in nums_dict.keys():
            if nums_dict[key] == maxi:
               return key
