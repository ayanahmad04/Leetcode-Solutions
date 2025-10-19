class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_n=bin(n)
        bin_list=list(bin_n)
        return bin_list.count('1')
