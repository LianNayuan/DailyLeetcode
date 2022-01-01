class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num = []
        while x:
            y = x % 10
            num.append(y)
            x = x // 10
        for i in range(len(num)//2):
            if num[i] != num[len(num)-i-1]:
                return False
        return True
