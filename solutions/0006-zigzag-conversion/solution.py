class Solution:
    def convert(self, s: str, numRows: int) -> str:
        x=list([] for _ in range(numRows))
        curr_row=0
        direction=1
        if numRows ==1 :
            return s
        for i in s:
            x[curr_row].append(i)
            if curr_row == 0:
                direction = +1
            elif curr_row == numRows-1:
                direction = -1
            curr_row+=direction
        st=[''.join(i) for i in x ]
        return ''.join(st)
