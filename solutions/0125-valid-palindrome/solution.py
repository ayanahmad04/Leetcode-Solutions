class Solution:
    def isPalindrome(self, s: str) -> bool:
        punctuations = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

        def remove_punc(text):
            result = ""
            for char in text:
                if char not in punctuations:
                    result += char
            return result
        
        cleaned_s = remove_punc(s)
        original=cleaned_s.lower().replace(" ","")
        if original == original[::-1]:
            return  True
        if original != original[::-1]:
            return False
        
