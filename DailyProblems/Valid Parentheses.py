class Solution:
    def isValid(self, s: str) -> bool:
        length = len(s)
        if length % 2 == 1:
            return False
        tmp = [0]
        for i in range(length):
            if s[i] == '(':
                tmp.append(s[i])
                continue
            elif s[i] == ')':
                if tmp[-1] == '(':
                    tmp.pop(-1)
                    continue
                else:
                    return False
            elif s[i] == '[':
                tmp.append(s[i])
                continue
            elif s[i] == ']':
                if tmp[-1] == '[':
                    tmp.pop(-1)
                    continue
                else:
                    return False
            elif s[i] == '{':
                tmp.append(s[i])
                continue
            elif s[i] == '}':
                if tmp[-1] == '{':
                    tmp.pop(-1)
                    continue
                else:
                    return False
        if len(tmp) == 1:
            return True
        else:
            return False
