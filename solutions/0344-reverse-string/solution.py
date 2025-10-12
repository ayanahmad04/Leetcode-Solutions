class Solution:
    def reverseString(self, s: list[str]) -> None:
        left=0
        right=len(s)-1
        difference=0
        while left<right:
            x=s[left]
            s[left]=s[right]
            s[right]=x
            left=left+1
            right=right-1
