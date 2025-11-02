class Solution:
    def intToRoman(self, num: int) -> str:
        romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        new_dict = dict(zip(romans.values(), romans.keys()))
        num_list = list(map(int, str(num)))
        fac = 1
        fac_nums = []
        for i in range(len(num_list)):
            fac_nums.append(fac)
            fac *= 10
        fac_nums = fac_nums[::-1]
        edge_cases = {
            900: "CM", 400: "CD",
            90: "XC", 40: "XL",
            9: "IX", 4: "IV"
        }
        aay = dict(zip(num_list, fac_nums))
        roman_map = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]
        final_str = ""
        val = num
        for value, symbol in roman_map:
            count = val // value          
            final_str += symbol * count    
            val -= value * count    
        return final_str
