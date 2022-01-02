class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        ast = [0] + sorted(asteroids)
        for i in range(len(ast)-1):
            if mass + ast[i] >= ast[i+1]:
                mass += ast[i]
            else:
                return False
        return True
