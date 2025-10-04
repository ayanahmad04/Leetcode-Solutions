class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_count = {}
        t_count = {}

        
        for ch in s:
            s_count[ch] = s_count.get(ch, 0) + 1
        
        
        for ch in t:
            t_count[ch] = t_count.get(ch, 0) + 1
        
        
        for ch in t_count:
            if ch not in s_count or t_count[ch] != s_count[ch]:
                return ch
        
     
