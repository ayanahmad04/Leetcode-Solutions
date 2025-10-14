class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_list=list(str(x))
        x_new=x_list.copy()
        x_new.reverse()
        if x_new == x_list :
            return True
        else:
            return False
