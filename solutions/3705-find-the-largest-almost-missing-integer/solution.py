class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:
        self.nums=nums
        self.k=k
        sub_arrays=[]
        noo=len(self.nums)-self.k+1
        for i in range(noo):
            sub_arrays.append(self.nums[i:i+self.k])
        new=dict.fromkeys(self.nums,0)
        for i in self.nums :
            count=0
            for x in sub_arrays:
                if i in x:
                    count=count+1
            new[i]=count
        maxx = -1
        for key,value in new.items():
            if value == 1:
                maxx = max(maxx, key)
        return maxx
