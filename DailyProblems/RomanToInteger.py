class Solution:
    def romanToInt(self,s: str) -> int:
        total = 0
        
        def FindInt(roman):
            if roman == 'I':
                return 1
            elif roman == 'V':
                return 5
            elif roman == 'X':
                return 10
            elif roman == 'L':
                return 50
            elif roman == 'C':
                return 100
            elif roman == 'D':
                return 500
            elif roman == 'M':
                return 1000
        
        ints = []
        for i in range(len(s)):
            ints.append(FindInt(s[i]))
        ints.append(0)
        
        for i in range(len(s)):
            if ints[len(s)-i-1] < ints[len(s)-i]:
                total -= ints[len(s)-i-1]
            else:
                total += ints[len(s)-i-1]
                
        return total
