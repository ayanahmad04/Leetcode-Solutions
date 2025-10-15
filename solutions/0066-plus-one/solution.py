class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        dgits_str="".join(map(str,digits))
        plus_one=int(dgits_str)+1
        new=list(map(int,str(plus_one)))
        return new
