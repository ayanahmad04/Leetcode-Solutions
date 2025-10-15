class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        s_list = list(s)
        count = 0
        for i in range(len(s_list)-1):
            if romans[s_list[i]] >= romans[s_list[i+1]]:
                count += romans[s_list[i]]
            else:
                count -= romans[s_list[i]]
        
        count += romans[s_list[-1]]
        return count
