class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        final_list = []
        temp_str = ''

        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        for i in range(len(s)):
            if s[i] not in temp_str:
                temp_str += s[i]
            else:
                final_list.append(temp_str)
                
                temp_str = temp_str[temp_str.index(s[i]) + 1:] + s[i]

        final_list.append(temp_str)  

        return max(map(len, final_list))
