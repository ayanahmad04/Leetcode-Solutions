class Solution:
    def frequencySort(self, s: str) -> str:
        s_dict = {}
        for ch in s:
            s_dict[ch] = s_dict.get(ch, 0) + 1
        
        sorted_items = sorted(s_dict.items(), key=lambda x: x[1], reverse=True)
        res = ''.join(ch * freq for ch, freq in sorted_items)
        return res
