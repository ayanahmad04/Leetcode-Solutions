class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list=list(s)
        t_list=list(t)
        s_dict={}
        for item in s_list:
                if item in s_dict:
                    s_dict[item] += 1
                else:
                    s_dict[item] = 1
        t_dict={}
        for item in t_list:
                if item in t_dict:
                    t_dict[item] += 1
                else:
                    t_dict[item] = 1
        return s_dict == t_dict
