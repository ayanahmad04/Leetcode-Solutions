class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
            twod=[]
            
            if m*n == len(original):
                for x in range(m):
                    twod.append(original[x*n:(x+1)*n])
                return twod
            
            else:
                return []
