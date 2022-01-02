class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]: 
        if m * n != len(original):
            target = []
        else:
            target = [[0 for col in range(n)] for row in range(m)]
            for j in range(m):
                target[j]= original[0:n]
                original = original[n:]
        return target
