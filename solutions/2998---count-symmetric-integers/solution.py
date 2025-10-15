class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low, high + 1):
            str_i = str(i)
            if len(str_i) % 2 == 0:
                midpoint = len(str_i) // 2
                if sum(map(int, str_i[:midpoint])) == sum(map(int, str_i[midpoint:])):
                    count += 1
        return count
