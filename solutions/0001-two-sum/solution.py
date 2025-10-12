class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        final_answer=[]
        x=0
        found=False
        while x<len(nums):
            for i in range(x,len(nums)-1):
                if nums[x] + nums[i+1] == target :
                    final_answer.append(x)
                    final_answer.append(i+1)
                    found=True
                    break
            if found :
               break
            if found == False:
               x=x+1
        return final_answer
