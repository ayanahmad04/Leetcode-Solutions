class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        temp = nums1[:m] + nums2   
        temp.sort()                
        

        for i in range(len(temp)):
            nums1[i] = temp[i]

