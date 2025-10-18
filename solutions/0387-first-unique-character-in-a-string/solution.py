class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_list=list(s)
        s_dict=dict.fromkeys(s_list,0)
        for i in s_list:
            s_dict[i]+=1
        
        flag = True
        for key,value in s_dict.items():
            if value ==1:
                flag=False
                return s_list.index(key)
                break
        if flag == True :
            return -1
