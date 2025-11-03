class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        pho = {
            2: ['a','b','c'],
            3: ['d','e','f'],
            4: ['g','h','i'],
            5: ['j','k','l'],
            6: ['m','n','o'],
            7: ['p','q','r','s'],
            8: ['t','u','v'],
            9: ['w','x','y','z'],
            0: [' ']
        }
        digits_list = list(map(int, digits))
        news = []
        
        for i in digits_list:
            news.append(pho[i])
        
        new = news[0]
        
        for k in range(1, len(news)):
            new = [x + y for x in new for y in news[k]]
        return new
