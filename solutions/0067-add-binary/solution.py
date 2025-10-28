class Solution:
    def addBinary(self, a: str, b: str) -> str:
        answer=int(a,2)+int(b,2)
        bin_ans=bin(answer)
        return bin_ans[2:]
