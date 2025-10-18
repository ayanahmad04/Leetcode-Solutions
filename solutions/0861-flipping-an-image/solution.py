class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        for x in range(len(image)):
            image[x].reverse()
            image[x]=[0 if i else 1 for i in image[x]]
        return image
