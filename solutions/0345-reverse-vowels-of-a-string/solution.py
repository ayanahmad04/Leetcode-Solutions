class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=['a','e','i','o','u','A','E','I','O','U']
        vowels_found=[]
        s_list=list(s)
        left = 0
        right =len(s_list)-1
        while left <right :
              if s_list[left] in vowels and s_list[right] in vowels:
                      s_list[left],s_list[right]=s_list[right],s_list[left]
                      left+=1
                      right-=1
              elif s_list[left] in vowels:
                      right-=1
              elif s_list[right] in vowels:
                      left+=1
              else :
                  left +=1
                  right -=1

        s_new=''.join(s_list)
        return s_new
