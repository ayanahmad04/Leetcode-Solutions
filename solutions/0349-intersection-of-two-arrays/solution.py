class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        intersection=[]
        for i in nums1:
            if i in nums2:
                intersection.append(i)
        intersection=list(set(intersection))
        return intersection
