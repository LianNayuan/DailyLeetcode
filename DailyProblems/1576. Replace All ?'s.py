# 看了评论区发现只要加头加尾就可以不判断边界，但是实践了一下还慢了4ms，有点离谱
class Solution:
    def modifyString(self, s: str) -> str:
        lst = ['a','b','c']
        s = list(s)

        if len(s) == 1:
            return 'a'

        if s[0] == '?':
            for i in range(len(lst)):
                if s[1] != lst[i]:
                    s[0] = lst[i]
                    break

        if s[-1] == '?':
            for i in range(len(lst)):
                if s[-2] != lst[i]:
                    s[-1] = lst[i]
                    break

        for j in range(1,len(s)-1):
            if s[j] == '?':
                for i in range(len(lst)):
                    if s[j - 1] != lst[i] and s[j + 1] != lst[i]:
                        s[j] = lst[i]
                        break


        return "".join(s)
        
        
