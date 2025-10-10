class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        s_new=[]
        t_new=[]
        for x,i in zip(s,t):
            s_new.append(x)
            t_new.append(i)
        s_dict=dict.fromkeys(s_new,None)
        t_dict=dict.fromkeys(t_new,None)
        for index,value in enumerate(zip(s_new,t_new)):
            s_dict[value[0]]=index
            t_dict[value[1]]=index
        x=0
        for key in s_dict.keys():
            e=abs(s_dict[key] - t_dict[key])
            x=e+x
        return x
