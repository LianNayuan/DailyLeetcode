class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        max = 0
        for i in range(len(s)):
            if s[i] == '(':
                count += 1
                if count > max:
                    max = count
            elif s[i] == ')':
                count -= 1
        return max
