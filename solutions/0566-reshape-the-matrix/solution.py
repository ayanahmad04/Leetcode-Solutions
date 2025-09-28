class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:  
        self.r=r
        self.c=c
        self.mat=mat
        new=[]
        for i in self.mat:
            for x in i:
                new.append(x)
        
        if len(new) == self.r*self.c:
            new_reshaped=[]
            y=0
            z=self.c
            for i in range(self.r):
                new_reshaped.append(new[y:z])
                y+=self.c
                z+=self.c
            return new_reshaped
        else :
            return self.mat
